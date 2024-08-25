import numpy as np
from geopandas import GeoDataFrame
from shapely import LineString

def linestring_to_lng_lat(linestring: LineString) -> list[list[float]]:
    POINTS = np.vstack(linestring.coords.xy).T.tolist()
    return POINTS

def lng_lat_to_linestring(points: list[list[float]]) -> LineString:
    return LineString(points)

def coordinates_to_wgs84(gdf: GeoDataFrame) -> GeoDataFrame:
    WGS84_GDF = gdf.to_crs(epsg=4326)
    return WGS84_GDF if type(WGS84_GDF) is GeoDataFrame else gdf

def split_multipart(gdf: GeoDataFrame) -> GeoDataFrame:
    SPLIT_GDF = gdf.explode()
    return SPLIT_GDF if type(SPLIT_GDF) is GeoDataFrame else gdf