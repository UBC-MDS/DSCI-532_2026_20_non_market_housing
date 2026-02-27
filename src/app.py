from ipyleaflet import Map, Marker
from shiny import App, ui, reactive, render
from shinywidgets import output_widget, render_widget
import pandas as pd
from shapely import wkt
from ipywidgets import HTML

clean_df = pd.read_csv(
    "data/processed/clean-non-market-housing.csv",
    dtype={"Occupancy Year": "Int64"}
    )
clean_df['Geom'] = clean_df['Geom'].apply(lambda x: wkt.loads(x) if isinstance(x, str) else None)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider(
                id="input_year",
                label="Occupancy Year",
                min=clean_df["Occupancy Year"].min(),
                max=clean_df["Occupancy Year"].max(),
                value=[clean_df["Occupancy Year"].min(), clean_df["Occupancy Year"].max()],
                sep=""
            ),
        bg="#f8f8f8"),
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

    @reactive.calc
    def filtered_df():
        #local_area = input.input_local_area()
        #operator = input.input_operator()
        year_min, year_max = input.input_year()
        #status = input.input_status()

        return clean_df.query(
            #"`Local Area` in @local_area & "
            #"`Operator` in @operator & "
            "`Occupancy Year` >= @year_min & "
            "`Occupancy Year` <= @year_max "
            #"`Project Status` in @status"
        )

    @render_widget
    def map():
        m = Map(center=(49.25, -123.12), zoom=12, scroll_wheel_zoom=True)
        df = filtered_df()
        
        if not df.empty:
            for _, row in df.iterrows():
                geom = row['Geom']
                if geom:
                    marker = Marker(location=(geom.y, geom.x), draggable=False)

                    marker.popup = HTML(f"""
                                <b>{row.get('Name', 'N/A')}</b><br>
                                <b>Address</b>: {row.get('Address', '')}<br>
                                <b>URL</b>: <a href="{row.get('URL', '')}" target="_blank">{row.get('URL', '')}</a>
                                """)
                    
                    m.add_layer(marker)
                    
        return m

app = App(app_ui, server=server)
