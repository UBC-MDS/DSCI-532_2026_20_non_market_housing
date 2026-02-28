import altair as alt
import pandas as pd

def make_occupancy_line_chart(d: pd.DataFrame) -> alt.Chart:
    """
    Build occupancy year line chart from a filtered dataframe.

    Expects column:
    - Occupancy Year
    Each row is treated as one development.
    """
    if "Occupancy Year" not in d.columns:
        return (
            alt.Chart(pd.DataFrame({"Occupancy Year": [], "Developments": []}))
            .mark_line()
            .encode(x="Occupancy Year:Q", y="Developments:Q")
            .properties(title="Developments by occupancy year", height=220, width="container")
        )

    tmp = d.copy()
    tmp["Occupancy Year"] = pd.to_numeric(tmp["Occupancy Year"], errors="coerce")
    tmp = tmp.dropna(subset=["Occupancy Year"])

    yearly = (
        tmp.groupby("Occupancy Year", as_index=False)
        .size()
        .rename(columns={"size": "Developments"})
        .sort_values("Occupancy Year")
    )

    # Viridis single color
    LINE_COLOR = "#31688e"

    chart = (
        alt.Chart(yearly)
        .mark_line(
            point=alt.OverlayMarkDef(filled=True, fill=LINE_COLOR),
            color=LINE_COLOR,
        )
        .encode(
            x=alt.X(
                "Occupancy Year:Q",
                title="Occupancy year",
                axis=alt.Axis(format="d"),
            ),
            y=alt.Y("Developments:Q", title="Number of developments"),
        )
        .properties(title="Developments by occupancy year", height=220, width="container")
        .configure_view(stroke=None)
        .configure_title(anchor="start")
    )
    return chart
