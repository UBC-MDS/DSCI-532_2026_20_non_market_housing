from shiny import App, ui

app_ui = ui.page_sidebar(
    ui.sidebar("Tabs/Views", bg="#f8f8f8"),
    ui.layout_columns(
        ui.layout_columns(
            ui.card("Chart/Metrics"),
            ui.card("Chart/Metrics"),
            ui.layout_columns(
                ui.card("Chart/Metrics"),
                ui.card("Chart/Metrics"),
                ui.card("Chart/Metrics"),
                col_widths=(6, 6, 12),
                row_heights=(1, 1),
            ),
            col_widths=(3, 3, 6),
        ),
        ui.layout_columns(
            ui.card("Map"),
            ui.card("Filters"),
            col_widths=(10, 2),
        ),
        col_widths=(12, 12),
        row_heights=(1, 3),
    ),
    fillable=True,
)


def server(input, output, session):
    pass


app = App(app_ui, server=server)
