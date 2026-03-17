import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.charts.clientele_bar_chart import prepare_clientele_totals


def test_prepare_clientele_totals_sums_numeric_values_correctly():
    """This test verifies that clientele totals are summed correctly because incorrect aggregation would make the bar chart misleading."""
    df = pd.DataFrame(
        {
            "Clientele - Families": [10, 5],
            "Clientele - Seniors": [3, 7],
            "Clientele - Other": [1, 2],
        }
    )

    result = prepare_clientele_totals(df)

    expected = pd.DataFrame(
        {
            "Clientele": ["Families", "Seniors", "Other"],
            "Units": [15, 10, 3],
        }
    )

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)


def test_prepare_clientele_totals_coerces_non_numeric_and_missing_to_zero():
    """This test verifies that invalid or missing values do not crash aggregation because dashboard data often contains blanks or mixed types."""
    df = pd.DataFrame(
        {
            "Clientele - Families": ["10", None],
            "Clientele - Seniors": ["bad", 4],
            "Clientele - Other": [1.5, None],
        }
    )

    result = prepare_clientele_totals(df)

    expected = pd.DataFrame(
        {
            "Clientele": ["Families", "Seniors", "Other"],
            "Units": [10.0, 4.0, 1.5],
        }
    )

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)


def test_prepare_clientele_totals_returns_zero_totals_when_columns_missing():
    """This test verifies graceful fallback when expected columns are absent because the chart should fail safely instead of breaking the dashboard."""
    df = pd.DataFrame({"Some Other Column": [1, 2, 3]})

    result = prepare_clientele_totals(df)

    expected = pd.DataFrame(
        {
            "Clientele": ["Families", "Seniors", "Other"],
            "Units": [0, 0, 0],
        }
    )

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)