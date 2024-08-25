from geopandas import GeoDataFrame
from shapely import LineString
import numpy as np

def sort_lng_lat(points: list[list[float]]) -> list[list[float]]:
    points.sort(key=lambda x: (x[1], x[0]))
    return points

def linestring_to_lng_lat(linestring: LineString) -> list[list[float]]:
    points = np.vstack(linestring.coords.xy).T.tolist()
    return sort_lng_lat(points)

def lng_lat_to_linestring(lng_lat: list[list[float]]) -> LineString:
    return LineString(lng_lat)

def coordinates_to_wgs84(gdf: GeoDataFrame) -> GeoDataFrame:
    converted_gdf = gdf.to_crs(epsg=4326)
    return converted_gdf if type(converted_gdf) is GeoDataFrame else gdf

def split_multipart(gdf: GeoDataFrame) -> GeoDataFrame:
    exploded_gdf = gdf.explode()
    return exploded_gdf if type(exploded_gdf) is GeoDataFrame else gdf