import altair as alt
import pandas as pd


CLIENTELE_COLS = [
    "Clientele - Families",
    "Clientele - Seniors",
    "Clientele - Other",
]

CLIENTELE_LABELS = {
    "Clientele - Families": "Families",
    "Clientele - Seniors": "Seniors",
    "Clientele - Other": "Other",
}


def prepare_clientele_totals(d: pd.DataFrame) -> pd.DataFrame:
    """
    Return a tidy dataframe of clientele unit totals for the bar chart.

    The function coerces clientele columns to numeric, treats missing values
    as zero, and returns totals for Families, Seniors, and Other.

    Parameters
    ----------
    d : pd.DataFrame
        Filtered dashboard dataframe.

    Returns
    -------
    pd.DataFrame
        A dataframe with columns:
        - Clientele
        - Units
    """
    missing = [c for c in CLIENTELE_COLS if c not in d.columns]
    if missing:
        return pd.DataFrame(
            {"Clientele": ["Families", "Seniors", "Other"], "Units": [0, 0, 0]}
        )

    tmp = d.copy()
    for c in CLIENTELE_COLS:
        tmp[c] = pd.to_numeric(tmp[c], errors="coerce").fillna(0)

    totals = (
        tmp[CLIENTELE_COLS]
        .sum()
        .rename_axis("Clientele")
        .reset_index(name="Units")
    )

    totals["Clientele"] = totals["Clientele"].replace(CLIENTELE_LABELS)

    return totals


def make_clientele_bar_chart(d: pd.DataFrame) -> alt.Chart:
    """
    Build clientele bar chart from a filtered dataframe.
    """
    totals = prepare_clientele_totals(d)

    chart = (
        alt.Chart(totals)
        .mark_bar()
        .encode(
            x=alt.X("Clientele:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y(
                "Units:Q", 
                title="Total units",
                axis=alt.Axis(format="~f")
            ),
            color=alt.Color("Clientele:N", scale=alt.Scale(scheme="viridis"), legend=None),
            tooltip=[
                alt.Tooltip("Clientele:N", title="Clientele"),
                alt.Tooltip("Units:Q", title="Total number of units", format=","),
            ],
        )
        .properties(title="Clientele unit totals", height="container", width="container")
        .configure_view(stroke=None)
        .configure_title(anchor="start")
    )

    return chart
