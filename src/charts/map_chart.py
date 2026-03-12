"""
Plotly map of Vancouver non-market housing with local area boundaries.
"""
import json
from pathlib import Path

import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
from shapely.geometry import shape


def _load_boundaries() -> gpd.GeoDataFrame:
    """Load Vancouver local area boundaries from CSV."""
    path = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "local-area-boundary.csv"
    df = pd.read_csv(path, sep=";")
    geometries = []
    for geom_str in df["Geom"]:
        geojson = json.loads(geom_str)
        geometries.append(shape(geojson))
    gdf = gpd.GeoDataFrame(df[["Name"]], geometry=geometries, crs="EPSG:4326")
    return gdf


def create_vancouver_map(df: pd.DataFrame) -> go.Figure:
    """
    Create a Plotly map showing Vancouver local areas and non-market housing projects.

    - Local area boundaries from local-area-boundary.csv
    - Project points from df (requires Geom column with WKT points)
    - Map bounds set to Vancouver
    """
    boundaries = _load_boundaries()

    # Build GeoJSON FeatureCollection for Choroplethmapbox
    features = []
    for _, row in boundaries.iterrows():
        geom = row.geometry
        if geom is None:
            continue
        # GeoJSON uses [lon, lat]
        geom_dict = geom.__geo_interface__
        features.append({
            "type": "Feature",
            "properties": {"name": row["Name"]},
            "geometry": geom_dict,
        })
    geojson = {"type": "FeatureCollection", "features": features}

    # Vancouver bounds (from boundary extent) with padding for more visible area
    bounds = boundaries.total_bounds  # minx, miny, maxx, maxy (lon, lat)
    pad = 0.097  # degrees padding on each side
    west = bounds[0] - pad
    east = bounds[2] + pad
    south = bounds[1] - pad
    north = bounds[3] + pad

    fig = go.Figure()

    # Add boundary outlines (Choroplethmapbox with transparent fill)
    fig.add_trace(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=boundaries["Name"].tolist(),
            z=[1] * len(boundaries),  # dummy for coloring
            featureidkey="properties.name",
            colorscale=[[0, "rgba(100, 149, 237, 0.15)"], [1, "rgba(100, 149, 237, 0.15)"]],
            showscale=False,
            marker_line_width=1.5,
            marker_line_color="rgba(70, 130, 180, 0.8)",
            hovertemplate="%{location}<extra></extra>",
            hoverlabel=dict(bgcolor="lightgray"),
        )
    )

    # Add project points
    points_df = df.dropna(subset=["Geom"]).copy()
    if not points_df.empty:
        points_df["lon"] = points_df["Geom"].apply(lambda g: g.x)
        points_df["lat"] = points_df["Geom"].apply(lambda g: g.y)
        def _url_part(r):
            url = r.get("URL", "")
            if pd.isna(url) or str(url).strip().lower() == "nan" or not str(url).strip():
                return ""
            return f"<br><a href='{url}' target='_blank'>view property</a>"

        hover_text = points_df.apply(
            lambda r: f"<b>{r.get('Name', 'N/A')}</b><br>"
            f"<b>Address</b>: {r.get('Address', '')}"
            + _url_part(r),
            axis=1,
        )
        fig.add_trace(
            go.Scattermapbox(
                lat=points_df["lat"],
                lon=points_df["lon"],
                mode="markers",
                marker=dict(size=10, color="#e74c3c", symbol="circle", opacity=0.9),
                text=hover_text,
                hoverinfo="text",
                name="Projects",
            )
        )

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=(south + north) / 2, lon=(west + east) / 2),
            zoom=10,
            bounds=dict(west=west, east=east, south=south, north=north),
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        height=450,
        hoverlabel=dict(bgcolor="white"),
    )

    return fig
