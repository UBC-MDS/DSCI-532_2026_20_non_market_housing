from pathlib import Path

from shiny import App, ui, reactive, render
from shinywidgets import output_widget, render_widget, render_altair
import pandas as pd
from shapely import wkt
import ibis
from ibis import _

from dotenv import load_dotenv
from querychat import init as querychat_init, sidebar as querychat_sidebar, server as querychat_server

load_dotenv()

from .charts.map_chart import create_vancouver_map
from .charts.accessibility_pie import create_accessibility_pie_chart
from .charts.clientele_bar_chart import make_clientele_bar_chart
from .charts.occupancy_line_chart import make_occupancy_line_chart
from .llm_client import get_querychat_client

con = ibis.duckdb.connect()
PARQUET = "data/processed/clean-non-market-housing.parquet"
housing = con.read_parquet(str(PARQUET))

local_area_choices: list[str] = sorted(
    housing.select("Local Area")
    .distinct()
    .execute()["Local Area"]
    .dropna()
    .tolist()
)

year_stats = (
    housing.select(
        min_year=housing["Occupancy Year"].min(),
        max_year=housing["Occupancy Year"].max(),
    )
    .execute()
    .iloc[0]
)
year_min_global = int(year_stats["min_year"])
year_max_global = int(year_stats["max_year"])

operator_choices: list[str] = sorted(
    housing.select("Operator")
    .distinct()
    .execute()["Operator"]
    .dropna()
    .tolist()
)

status_choices = {
                    "Proposed": "Proposed",
                    "Approved": "Approved",
                    "Under Construction": "Under Construction",
                    "Completed": "Completed"
                }


querychat_df = housing.drop(["Geom"]).execute()
project_root = Path(__file__).resolve().parent.parent
_querychat_client = get_querychat_client()
qc_params = {
    "greeting": project_root / "greeting.md",
    "data_description": project_root / "data_description.md",
}
if _querychat_client is not None:
    qc_params["client"] = _querychat_client
qc_config = querychat_init(querychat_df, "non_market_housing", **qc_params)




dashboard_content = [
    ui.tags.style("""
    .selectize-input {
        border-color: #6c757d !important;
    }

    .shiny-input-checkboxgroup input[type="checkbox"]:not(:checked),
    .shiny-input-checkbox:not(:checked) {
        border-color: #6c757d !important;
    }

    .bslib-value-box,
    .bslib-value-box .card-body {
        padding-top: 0 !important;
    }

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

    /* Keep Plotly map hover tooltip stable when cursor is over it */
    .map-widget-container .hoverlayer,
    .map-widget-container .hoverlayer *,
    .map-widget-container .hoverlayer path,
    .map-widget-container .hoverlayer .hovertext,
    .map-widget-container .hoverlayer .hoverlabel {
        pointer-events: auto !important;
    }
    """),
            ui.layout_columns(
                ui.layout_columns(
                ui.layout_columns(
                ui.layout_columns(
                    ui.value_box(
                        title="Total Projects",
                        value=ui.output_text("total_count"),
                    ),
                    ui.value_box(
                        title="Total Units",
                        value=ui.output_text("total_units"),
                    ),
                    col_widths=(6, 6),
                ),
                ui.card(
                    output_widget("clientele_bar", width="100%", fill=True),
                    style="overflow: hidden;",
                ),
                col_widths=(12, 12),
                row_heights=(0.7, 2.7),
            ),
            ui.card(
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
            ui.card(
                ui.div(
                    output_widget("map"),
                    class_="map-widget-container",
                ),
            ),
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
        choices=local_area_choices,
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
        "input_year", "Occupancy Year",
        min=year_min_global, max=year_max_global,
        value=[year_min_global, year_max_global],
        sep=""
    ),
    title="Filters",
    bg="#f8f8f8",
)

app_ui = ui.page_navbar(
    ui.nav_panel("Dashboard", ui.layout_sidebar(filters_sidebar, *dashboard_content, fillable=True)),
    ui.nav_panel(
        "Assistant",
        ui.layout_sidebar(
            querychat_sidebar("querychat", position="right", open="always"),
            ui.layout_columns(
                ui.layout_columns(
                    ui.layout_columns(
                        ui.card(
                            output_widget("qc_clientele_bar", width="100%", fill=True),
                        ),
                        ui.download_button(
                            "download_view", "⬇ Download filtered view", class_="btn-primary"
                        ),
                        col_widths=(12, 12),
                        row_heights=(5, 1),
                    ),
                    ui.card(
                        output_widget("qc_accessibility_pie", width="100%", fill=True),
                    ),
                    col_widths=(6, 6)
                ),
                ui.card(
                    ui.card_header(ui.output_text("qc_title")),
                    ui.output_data_frame("qc_table"),
                    fill=True,
                ),
                col_widths=(12, 12),
                row_heights=(2, 3),
            ),
            fillable=True,
        ),
        value="assistant",
    ),
    title="Non-Market Housing",
    fillable=True,
    theme=ui.Theme("lux"),
)


def server(input, output, session):
    qc_vals = querychat_server("querychat", querychat_config=qc_config)
    map_selection = reactive.Value(None)

    @render.text
    def qc_title():
        return qc_vals.title() or "Non-Market Housing Data"

    @render.data_frame
    def qc_table():
        df = qc_vals.df().copy()

        df["URL"] = df["URL"].apply(
            lambda x: ui.a(x, href=x, target="_blank") if x else ""
        )

        return df

    @reactive.calc
    def filtered_df() -> pd.DataFrame:
        local_area = list(input.input_local_area()) or local_area_choices
        operator = list(input.input_operator()) or operator_choices
        status = list(input.input_status()) or list(status_choices.keys())
        include_unocc = input.input_occupied()
        year_min, year_max = input.input_year()

        expr = housing

        expr = expr.filter(expr["Local Area"].isin(local_area))
        expr = expr.filter(expr["Operator"].isin(operator))
        expr = expr.filter(expr["Project Status"].isin(status))

        year_col = expr["Occupancy Year"]
        in_range = year_col.between(year_min, year_max)

        if include_unocc:
            expr = expr.filter(year_col.isnull() | in_range)
        else:
            expr = expr.filter(in_range)

        df = expr.execute()

        if "Geom" in df.columns:
            df["Geom"] = df["Geom"].apply(
                lambda x: wkt.loads(x) if isinstance(x, str) else None
            )

        return df

    @reactive.calc
    def display_df():
        """Filtered data combined with map lasso selection."""
        df = filtered_df()
        selected = map_selection()
        if selected is not None and len(selected) > 0:
            return df.loc[df.index.intersection(selected)]
        return df

    @render_widget
    def map():
        map_selection.set(None)  # reset selection when filters change
        return create_vancouver_map(filtered_df(), selection_handler=map_selection)
    
    @render_altair(width="100%", height="100%", fill=True)
    def accessibility_pie_chart():
        return create_accessibility_pie_chart(display_df())
    
    @render.text
    def total_count():
        return str(len(display_df()))

    @render.text
    def total_units():
        df = display_df()
        unit_cols = ["Adaptable", "Accessible", "Standard"]
        if all(c in df.columns for c in unit_cols):
            total = df[unit_cols].fillna(0).astype(float).sum().sum()
            return f"{int(total):,}"
        return "0"

    @render_altair
    def clientele_bar():
        return make_clientele_bar_chart(display_df())

    @render_altair
    def occupancy_line():
        return make_occupancy_line_chart(display_df())
    
    @render.download(filename="non_market_housing_filtered.csv")
    def download_view():
        yield qc_table.data_view().to_csv(index=False)

    @render_altair
    def qc_clientele_bar():
        df = qc_vals.df().copy()
        return make_clientele_bar_chart(df)

    @render_altair(width="100%", height="100%", fill=True)
    def qc_accessibility_pie():
        df = qc_vals.df().copy()
        return create_accessibility_pie_chart(df)

app = App(app_ui, server=server)