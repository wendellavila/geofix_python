import math
from geopandas import GeoDataFrame
from shapely import LineString

from lib import converter

def _haversine_distance(start: list[float], end: list[float]) -> float:
    R = 6371 # Radius of the earth in km (Volumetric mean radius)
    P = math.pi / 180

    START_LAT = start[1]
    START_LNG = start[0]
    END_LAT = end[1]
    END_LNG = end[0]

    A = 0.5 - math.cos((END_LAT - START_LAT) * P) / 2 + \
        math.cos(START_LAT * P) * \
        math.cos(END_LAT * P) * \
        (1 - math.cos((END_LNG - START_LNG) * P)) / 2
    
    return 2 * R * math.asin(math.sqrt(A))

def _linestring_length(points: list[list[float]]) -> float:
    total_length = 0.0

    for i in range (0, len(points) - 1):
      START = points[i]
      END = points[i+1]
      total_length += _haversine_distance(START, END)
      
    return total_length

def connect_gaps(gdf: GeoDataFrame) -> GeoDataFrame:
    gdf['coordinates'] = gdf.apply(converter.linestring_to_lng_lat)

    #

    gdf.drop('coordinates', axis=1)
    return gdf