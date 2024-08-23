from geopandas import GeoDataFrame
from shapely import LineString
import numpy as np

def line_string_to_points(line_string: LineString) -> list:
    return np.vstack(line_string.coords.xy).T.tolist()

def coordinates_to_wgs84(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf.to_crs(epsg=4326)

def split_multipart(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf.explode()