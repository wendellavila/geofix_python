from geopandas import GeoDataFrame
from lib import converter

def has_lines(gdf: GeoDataFrame) -> bool:
    line_string = gdf.at[0, 'geometry']
    points = converter.line_string_to_points(line_string)
    return True if len(points) == 2 else False

def connect_lines(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf

def connect_curves(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf

def connect_gaps(gdf: GeoDataFrame) -> GeoDataFrame:
    return connect_lines(gdf) if has_lines(gdf) else connect_curves(gdf) 