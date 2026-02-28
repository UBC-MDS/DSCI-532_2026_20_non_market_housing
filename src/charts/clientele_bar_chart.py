import altair as alt
import pandas as pd

def make_clientele_bar_chart(d: pd.DataFrame) -> alt.Chart:
    """
    Build clientele bar chart from a filtered dataframe.

    Expects these columns to exist (unit counts):
    - Clientele - Families
    - Clientele - Seniors
    - Clientele - Other
    """
    cols = ["Clientele - Families", "Clientele - Seniors", "Clientele - Other"]

    missing = [c for c in cols if c not in d.columns]
    if missing:
        return (
            alt.Chart(pd.DataFrame({"Clientele": [], "Units": []}))
            .mark_bar()
            .encode(x="Clientele:N", y="Units:Q")
            .properties(title="Clientele unit totals", height=220, width="container")
        )

    tmp = d.copy()
    for c in cols:
        tmp[c] = pd.to_numeric(tmp[c], errors="coerce").fillna(0)

    totals = (
        tmp[cols].sum()
        .rename_axis("Clientele")
        .reset_index(name="Units")
        .replace(
            {
                "Clientele - Families": "Families",
                "Clientele - Seniors": "Seniors",
                "Clientele - Other": "Other",
            }
        )
    )

    chart = (
        alt.Chart(totals)
        .mark_bar()
        .encode(
            x=alt.X("Clientele:N", title=None),
            y=alt.Y("Units:Q", title="Total units"),
            color=alt.Color("Clientele:N", scale=alt.Scale(scheme="viridis"), legend=None),
        )
        .properties(title="Clientele unit totals", height=220, width="container")
        .configure_view(stroke=None)
        .configure_title(anchor="start")
    )

    return chart
