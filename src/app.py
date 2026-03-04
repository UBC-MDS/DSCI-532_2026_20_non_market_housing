from ipyleaflet import Map, Marker, LayerGroup
from shiny import App, ui, reactive, render
from shinywidgets import output_widget, render_widget, render_altair
import pandas as pd
from shapely import wkt
from ipywidgets import HTML

from .charts.accessibility_pie import create_accessibility_pie_chart
from .charts.clientele_bar_chart import make_clientele_bar_chart
from .charts.occupancy_line_chart import make_occupancy_line_chart

clean_df = pd.read_csv(
    "data/processed/clean-non-market-housing.csv",
    dtype={"Occupancy Year": "Int64"}
    )

clean_df['Geom'] = clean_df['Geom'].apply(lambda x: wkt.loads(x) if isinstance(x, str) else None)
local_areas = sorted(clean_df["Local Area"].unique().tolist())

status_choices = {
                    "Proposed": "Proposed",
                    "Approved": "Approved",
                    "Under Construction": "Under Construction",
                    "Completed": "Completed"
                }
operator_choices = {v: v for v in sorted(clean_df["Operator"].dropna().unique())}

dashboard_content = [
    ui.tags.style("""
    .accessibility-card,
    .accessibility-card .card-body,
    .accessibility-card .html-fill-item {
        overflow: hidden !important;
    }

    .accessibility-card .card-body {
        display: flex;
        justify-content: center;
        padding: 1rem 0.75rem 0.5rem 0.75rem;
    }

    .accessibility-chart-wrap {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
    }

    #accessibility_pie_chart,
    #accessibility_pie_chart .vega-embed {
        width: 100% !important;
        height: 100% !important;
    }
    """),
    ui.layout_columns(
        ui.layout_columns(
            ui.layout_columns(
                ui.value_box(
                title="Total Projects",
                value=ui.output_text("total_count"),
                ),
                ui.card(
                    ui.card_header("Clientele Bar Chart"),
                    output_widget("clientele_bar", width="100%", fill=True),
                    style="overflow: hidden;",
                ),
                col_widths=(12, 12),
                row_heights=(0.7, 2.7),
            ),
            ui.card(
                ui.card_header("Occupancy Year Line Chart"),
                output_widget("occupancy_line", width="100%", fill=True),
                style="overflow: hidden;"
            ),
            ui.card(
                ui.div(
                    output_widget(
                        "accessibility_pie_chart",
                        width="100%",
                        height="100%",
                        fill=True,
                    ),
                    class_="accessibility-chart-wrap",
                ),
                class_="accessibility-card",
            ),
            col_widths=(4, 5, 3),
        ),
        ui.layout_columns(
            ui.card(output_widget("map")),
            col_widths=(12,),
        ),
        col_widths=(12, 12),
        row_heights=(2, 3),
    ),
]

filters_sidebar = ui.sidebar(
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
            selected=[]
    ),
    ui.input_selectize(
        "input_operator",
        "Operator",
        operator_choices,
        multiple=True
    ),
    ui.input_checkbox("input_occupied", "Include Unoccupied Projects", True),
    ui.input_slider(
            id="input_year",
            label="Occupancy Year",
            min=clean_df["Occupancy Year"].min(),
            max=clean_df["Occupancy Year"].max(),
            value=[clean_df["Occupancy Year"].min(), clean_df["Occupancy Year"].max()],
            sep=""
        ),
    title="Filters",
    bg="#f8f8f8",
)

app_ui = ui.page_navbar(
    ui.nav_panel("Dashboard", ui.layout_sidebar(filters_sidebar, *dashboard_content, fillable=True)),
    ui.nav_panel("Assistant", ui.card("Content for tab B")),
    title="Non-Market Housing",
    fillable=True,
    theme=ui.Theme("lux"),
)


def server(input, output, session):

    @reactive.calc
    def filtered_df():
        local_area = input.input_local_area()
        operator = input.input_operator()
        include_unoccupied = input.input_occupied()
        year_min, year_max = input.input_year()
        status = input.input_status()

        if not local_area:
            local_area = local_areas
        if not status:
            status = list(status_choices.keys())
        if not operator:
            operator = list(operator_choices.keys())

        filtered = clean_df.copy().query(
            "`Local Area` in @local_area & "
            "`Operator` in @operator & "
            "`Project Status` in @status"
        )

        if include_unoccupied:
            year_mask = (
                filtered["Occupancy Year"].isna() |
                (filtered["Occupancy Year"].between(
                    year_min, year_max, inclusive="both"))
            )
        else:
            year_mask = filtered["Occupancy Year"].between(
                year_min, year_max, inclusive="both"
            )

        return filtered[year_mask]

    @render_widget
    def map():
        df = filtered_df()
        m = Map(center=(49.25, -123.12), zoom=12, scroll_wheel_zoom=True)
        
        for _, row in df.dropna(subset=['Geom']).iterrows():
            geom = row['Geom']
            marker = Marker(location=(geom.y, geom.x), draggable=False)
            marker.popup = HTML(f"""
                <b>{row.get('Name', 'N/A')}</b><br>
                <b>Address</b>: {row.get('Address', '')}<br>
                <b>URL</b>: <a href="{row.get('URL', '')}" target="_blank">{row.get('URL', '')}</a>
            """)
            m.add_layer(marker)
        
        return m
    
    @render_altair(width="100%", height="100%", fill=True)
    def accessibility_pie_chart():
        return create_accessibility_pie_chart(filtered_df())
    
    @render.text
    def total_count():
        return str(len(filtered_df()))

    @render_altair
    def clientele_bar():
        return make_clientele_bar_chart(filtered_df())

    @render_altair
    def occupancy_line():
        return make_occupancy_line_chart(filtered_df())

app = App(app_ui, server=server)