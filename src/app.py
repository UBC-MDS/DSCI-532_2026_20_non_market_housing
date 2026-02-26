from ipyleaflet import Map
from shiny import App, ui
from shinywidgets import output_widget, render_widget

app_ui = ui.page_sidebar(
    ui.sidebar("Filters", bg="#f8f8f8"),
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
)


def server(input, output, session):
    @render_widget
    def map():
        return Map(
            center=(49.25, -123.12),
            zoom=12.2,
            min_zoom=12.2,
            scroll_wheel_zoom=True,
        )


app = App(app_ui, server=server)
