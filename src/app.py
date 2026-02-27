from ipyleaflet import Map, Marker
from shiny import App, ui, reactive
from shinywidgets import output_widget, render_widget
import pandas as pd
import altair as alt
from shapely import wkt
from ipywidgets import HTML

clean_df = pd.read_csv(
    "data/processed/clean-non-market-housing.csv",
    dtype={"Occupancy Year": "Int64"},
)

clean_df["Geom"] = clean_df["Geom"].apply(lambda x: wkt.loads(x) if isinstance(x, str) else None)

local_areas = sorted(clean_df["Local Area"].dropna().unique().tolist())

status_choices = {
    "Proposed": "Proposed",
    "Approved": "Approved",
    "Under Construction": "Under Construction",
    "Completed": "Completed",
}
operator_choices = {v: v for v in sorted(clean_df["Operator"].dropna().unique())}

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_selectize(
            id="input_local_area",
            label="Local Area",
            choices=local_areas,
            multiple=True,
        ),
        ui.input_checkbox_group(
            id="input_status",
            label="Project Status",
            choices=status_choices,
            selected=[],
        ),
        ui.input_selectize(
            "input_operator",
            "Operator",
            operator_choices,
            multiple=True,
        ),
        ui.input_slider(
            id="input_year",
            label="Occupancy Year",
            min=clean_df["Occupancy Year"].min(),
            max=clean_df["Occupancy Year"].max(),
            value=[clean_df["Occupancy Year"].min(), clean_df["Occupancy Year"].max()],
            sep="",
        ),
        title="Filters",
        bg="#f8f8f8",
    ),
    ui.layout_columns(
        ui.layout_columns(
            ui.layout_columns(
                ui.card("Total count"),
                ui.card("Clientele Bar Chart"), 
                col_widths=(12, 12),
                row_heights=(1, 2),
            ),
            ui.card(output_widget("occupancy_line")),
            ui.card("Design Pie Chart"),
            col_widths=(4, 5, 3),
        ),
        ui.layout_columns(
            ui.card(output_widget("map")),
            col_widths=(12,),
        ),
        col_widths=(12, 12),
        row_heights=(2, 3),
    ),
    fillable=True,
    theme=ui.Theme("lux"),
)

def server(input, output, session):

    @reactive.calc
    def filtered_df():
        local_area = input.input_local_area()
        operator = input.input_operator()
        year_min, year_max = input.input_year()
        status = input.input_status()

        if not local_area:
            local_area = local_areas
        if not operator:
            operator = list(operator_choices.keys())
        if not status:
            status = list(status_choices.keys())

        return clean_df.query(
            "`Local Area` in @local_area & "
            "`Operator` in @operator & "
            "((`Occupancy Year`.isna()) | ((`Occupancy Year` >= @year_min) & (`Occupancy Year` <= @year_max))) & "
            "`Project Status` in @status"
        )

    @render_widget
    def map():
        d = filtered_df()
        m = Map(center=(49.25, -123.12), zoom=12, scroll_wheel_zoom=True)

        for _, row in d.dropna(subset=["Geom"]).iterrows():
            geom = row["Geom"]
            marker = Marker(location=(geom.y, geom.x), draggable=False)
            marker.popup = HTML(
                f"""
                <b>{row.get('Name', 'N/A')}</b><br>
                <b>Address</b>: {row.get('Address', '')}<br>
                <b>URL</b>: <a href="{row.get('URL', '')}" target="_blank">{row.get('URL', '')}</a>
                """
            )
            m.add_layer(marker)

        return m

    @render_widget
    def occupancy_line():
        d = filtered_df().dropna(subset=["Occupancy Year"]).copy()

        yearly = (
            d.groupby("Occupancy Year", as_index=False)
            .size()
            .rename(columns={"size": "Developments"})
            .sort_values("Occupancy Year")
        )

        LINE_COLOR = "#31688e"

        chart = (
            alt.Chart(yearly)
            .mark_line(
                point=alt.OverlayMarkDef(filled=True, fill=LINE_COLOR),
                color=LINE_COLOR
            )
            .encode(
                x=alt.X("Occupancy Year:Q", title="Occupancy year", axis=alt.Axis(format="d")),
                y=alt.Y("Developments:Q", title="Number of developments"),
            )
            .properties(title="Developments by occupancy year", height=220, width="container")
            .configure_view(stroke=None)
            .configure_title(anchor="start")
        )
        return chart