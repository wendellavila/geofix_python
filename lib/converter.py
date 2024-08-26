import numpy as np
from geopandas import GeoDataFrame
from shapely import LineString

def linestring_to_lng_lat(linestring: LineString) -> list[list[float]]:
    """
    Converte LineStrings para lista de coordenadas no formato [lng, lat].

    :param LineString linestring: Uma LineString criada pela biblioteca shapely.
    :return coordinates: Uma lista de coordenadas no formato [lng, lat].
    """
    return np.vstack(linestring.coords.xy).T.tolist()

def lng_lat_to_linestring(points: list[list[float]]) -> LineString:
    """
    Converte uma lista de coordenadas no formato [lng, lat] para LineString.
    
    :param list[list[float]] coordinates: Uma lista de coordenadas no formato [lng, lat].
    :return linestring: Uma LineString criada pela biblioteca shapely.
    """
    return LineString(points)

def coordinates_to_wgs84(gdf: GeoDataFrame) -> GeoDataFrame:
    """
    Converte as coordenadas de um GeoDataFrame para WGS84 (EPSG:4326).

    :param GeoDataFrame gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :return gdf: Um GeoDataFrame contendo apenas coordenadas no formato WGS84.
    """
    WGS84_GDF = gdf.to_crs(epsg=4326)
    return WGS84_GDF if type(WGS84_GDF) is GeoDataFrame else gdf

def split_multipart(gdf: GeoDataFrame) -> GeoDataFrame:
    """
    Converte tipos geométricos de múltiplas partes para múltiplos tipos geométricos de parte única.

    :param GeoDataFrame gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :return gdf: Um GeoDataFrame contendo apenas tipos geométricos de parte única.
    """
    SPLIT_GDF = gdf.explode()
    return SPLIT_GDF if type(SPLIT_GDF) is GeoDataFrame else gdf