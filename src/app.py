from ipyleaflet import Map
from shiny import App, ui, reactive, render
from shinywidgets import output_widget, render_widget
import pandas as pd

clean_df = pd.read_csv(
    "data/processed/clean-non-market-housing.csv",
    dtype={"Occupancy Year": "Int64"}
    )

status_choices = {
                    "Proposed": "Proposed",
                    "Approved": "Approved",
                    "Under Construction": "Under Construction",
                    "Completed": "Completed"
                }

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_checkbox_group(
                id="input_status",
                label="Project Status",
                choices=status_choices,
                selected=[]
        ),
        ui.input_slider(
                id="input_year",
                label="Occupancy Year",
                min=clean_df["Occupancy Year"].min(),
                max=clean_df["Occupancy Year"].max(),
                value=[clean_df["Occupancy Year"].min(), clean_df["Occupancy Year"].max()],
                sep=""
        )
    ),
    ui.layout_columns(
        ui.layout_columns(
            ui.layout_columns(
                ui.card("Total count"),
                ui.card("Clientele Bar Chart"),
                col_widths=(12, 12),
                row_heights=(1, 2),
            ),
            ui.card("Occupancy Year Line Chart"),
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
    theme=ui.Theme("lux")
)


def server(input, output, session):

    @reactive.calc
    def filtered_df():
        local_area = input.input_local_area()
        operator = input.input_operator()
        year_min, year_max = input.input_year()
        status = input.input_status()
        if not status:
            status = list(status_choices.keys())

        return clean_df.query(
            "`Local Area` in @local_area & "
            "`Operator` in @operator & "
            "`Occupancy Year` >= @year_min & "
            "`Occupancy Year` <= @year_max & "
            "`Project Status` in @status"
        )
    
    @render_widget
    def map():
        return Map(
            center=(49.25, -123.12),
            zoom=12.2,
            min_zoom=12.2,
            scroll_wheel_zoom=True,
        )


app = App(app_ui, server=server)
