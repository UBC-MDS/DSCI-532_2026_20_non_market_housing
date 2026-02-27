import pandas as pd
import altair as alt

accessibility_pie_colors = {
    "Adaptable": "#5B8DEF",
    "Accessible": "#4ECDC4",
    "Standard": "#6C5B7B",
    "No data": "#BDC3C7",
}

ACCESSIBILITY_COL_MAP = {
    "Accessible": [
        "Design - Accessible 1BR", "Design - Accessible 2BR",
        "Design - Accessible 3BR", "Design - Accessible 4BR",
        "Design - Accessible Studio", "Design - Accessible Room",
    ],
    "Adaptable": [
        "Design - Adaptable 1BR", "Design - Adaptable 2BR",
        "Design - Adaptable 3BR", "Design - Adaptable 4BR",
    ],
    "Standard": [
        "Design - Standard 1BR", "Design - Standard 2BR",
        "Design - Standard 3BR", "Design - Standard 4BR",
        "Design - Standard Studio", "Design - Standard Room",
    ],
}


def create_accessibility_pie_chart(df: pd.DataFrame) -> alt.Chart:
    """Create an accessibility pie chart from filtered housing data."""
    rows = []
    for accessibility, cols in ACCESSIBILITY_COL_MAP.items():
        units = df[cols].sum().sum()
        if units > 0:
            br1 = int(df[cols[0]].sum()) if len(cols) > 0 else 0
            br2 = int(df[cols[1]].sum()) if len(cols) > 1 else 0
            br3 = int(df[cols[2]].sum()) if len(cols) > 2 else 0
            br4 = int(df[cols[3]].sum()) if len(cols) > 3 else 0
            studio = int(df[cols[4]].sum()) if len(cols) > 4 else 0
            room = int(df[cols[5]].sum()) if len(cols) > 5 else 0
            rows.append({
                "Accessibility": accessibility,
                "Units": units,
                "1BR": br1,
                "2BR": br2,
                "3BR": br3,
                "4BR": br4,
                "Studio": studio,
                "Room": room,
            })

    chart_data = pd.DataFrame(rows)
    if chart_data.empty:
        chart_data = pd.DataFrame({
            "Accessibility": ["No data"],
            "Units": [1],
            "1BR": [0], "2BR": [0], "3BR": [0], "4BR": [0], "Studio": [0], "Room": [0],
        })

    return (
        alt.Chart(chart_data)
        .mark_arc(innerRadius=70, outerRadius=120)
        .encode(
            theta=alt.Theta("Units:Q", stack=True),
            color=alt.Color(
                "Accessibility:N",
                scale=alt.Scale(
                    domain=list(accessibility_pie_colors.keys()),
                    range=list(accessibility_pie_colors.values()),
                ),
                legend=alt.Legend(title=None, orient="bottom"),
            ),
            tooltip=[
                alt.Tooltip("Accessibility:N", title="Category"),
                alt.Tooltip("Units:Q", title="Total number of units", format=","),
                alt.Tooltip("1BR:Q", title="1 Bedroom", format=","),
                alt.Tooltip("2BR:Q", title="2 Bedroom", format=","),
                alt.Tooltip("3BR:Q", title="3 Bedroom", format=","),
                alt.Tooltip("4BR:Q", title="4 Bedroom", format=","),
                alt.Tooltip("Studio:Q", title="Studio", format=","),
                alt.Tooltip("Room:Q", title="Individual Room", format=","),
            ],
        )
        .properties(
            width=300,
            height=250,
            usermeta={"embedOptions": {"actions": False}},
        )
        .configure_view(strokeWidth=0)
        .configure_axis(domain=False, grid=False)
        .configure_legend(labelFontSize=12, titleFontSize=14)
    )
