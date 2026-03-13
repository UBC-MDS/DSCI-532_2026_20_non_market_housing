from pathlib import Path
import re

import pandas as pd
import pytest


DATA_PATH = Path("data/processed/clean-non-market-housing.csv")


def load_data():
    return pd.read_csv(DATA_PATH, dtype={"Occupancy Year": "Int64"})


def apply_dashboard_filters(
    df,
    local_area=None,
    status=None,
    operator=None,
    include_unoccupied=True,
    year_min=None,
    year_max=None,
):
    local_areas = sorted(df["Local Area"].dropna().unique().tolist())
    operators = sorted(df["Operator"].dropna().unique().tolist())
    statuses = ["Proposed", "Approved", "Under Construction", "Completed"]

    if not local_area:
        local_area = local_areas
    if not status:
        status = statuses
    if not operator:
        operator = operators

    filtered = df.copy().query(
        "`Local Area` in @local_area & `Operator` in @operator & `Project Status` in @status"
    )

    if include_unoccupied:
        year_mask = (
            filtered["Occupancy Year"].isna()
            | filtered["Occupancy Year"].between(year_min, year_max, inclusive="both")
        )
    else:
        year_mask = filtered["Occupancy Year"].between(
            year_min, year_max, inclusive="both"
        )

    return filtered[year_mask]


def expected_total_units(df):
    unit_cols = ["Adaptable", "Accessible", "Standard"]
    if all(c in df.columns for c in unit_cols):
        return int(df[unit_cols].fillna(0).astype(float).sum().sum())
    return 0


def read_kpi_value(page, label):
    text = page.locator("body").inner_text()
    match = re.search(rf"{re.escape(label)}\s+([\d,]+)", text)
    assert match, f"Could not find KPI value for '{label}' on page"
    return int(match.group(1).replace(",", ""))


def choose_single_selectize_option(page, label, value):
    page.get_by_label(label).click()
    page.get_by_text(value, exact=True).click()
    page.keyboard.press("Escape")


def check_single_status(page, value):
    page.get_by_label(value, exact=True).check()


def find_zero_result_area_status_pair(df):
    local_areas = sorted(df["Local Area"].dropna().unique().tolist())
    statuses = ["Proposed", "Approved", "Under Construction", "Completed"]

    for area in local_areas:
        for status in statuses:
            subset = df[
                (df["Local Area"] == area)
                & (df["Project Status"] == status)
            ]
            if len(subset) == 0:
                return area, status

    return None, None


def test_dashboard_default_total_projects_matches_data(page, live_server):
    """This test verifies the default Total Projects value matches the dataset because it confirms the dashboard loads with the correct initial filter state."""
    df = load_data()
    year_min = int(df["Occupancy Year"].min())
    year_max = int(df["Occupancy Year"].max())

    expected = len(
        apply_dashboard_filters(
            df,
            local_area=None,
            status=None,
            operator=None,
            include_unoccupied=True,
            year_min=year_min,
            year_max=year_max,
        )
    )

    page.goto(live_server.url)
    page.wait_for_load_state("networkidle")

    actual = read_kpi_value(page, "Total Projects")
    assert actual == expected


def test_local_area_filter_updates_total_units_correctly(page, live_server):
    """This test verifies aggregation correctness by checking that Total Units updates to the expected sum after filtering by Local Area."""
    df = load_data()
    year_min = int(df["Occupancy Year"].min())
    year_max = int(df["Occupancy Year"].max())

    chosen_area = sorted(df["Local Area"].dropna().unique().tolist())[0]

    expected_df = apply_dashboard_filters(
        df,
        local_area=[chosen_area],
        status=None,
        operator=None,
        include_unoccupied=True,
        year_min=year_min,
        year_max=year_max,
    )
    expected_units = expected_total_units(expected_df)

    page.goto(live_server.url)
    page.wait_for_load_state("networkidle")

    choose_single_selectize_option(page, "Local Area", chosen_area)
    page.wait_for_timeout(1000)

    actual_units = read_kpi_value(page, "Total Units")
    assert actual_units == expected_units


def test_edge_case_filter_combination_can_return_zero_projects(page, live_server):
    """This test verifies an edge-case filter combination can safely return zero projects because the dashboard should handle empty subsets without breaking."""
    df = load_data()

    area, status = find_zero_result_area_status_pair(df)
    assert area is not None and status is not None, (
        "Could not find a Local Area + Project Status combination with zero rows "
        "in the dataset."
    )

    page.goto(live_server.url)
    page.wait_for_load_state("networkidle")

    choose_single_selectize_option(page, "Local Area", area)
    check_single_status(page, status)
    page.wait_for_timeout(1000)

    actual_projects = read_kpi_value(page, "Total Projects")
    assert actual_projects == 0