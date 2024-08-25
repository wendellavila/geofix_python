import math
import shapely
import numpy as np

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

def _combine_points(a: LineString, b: LineString) -> list[list[float]]:
    a_list = converter.linestring_to_lng_lat(a)
    b_list = converter.linestring_to_lng_lat(b)
    return a_list + b_list

def _recursive_merge_rows(gdf: GeoDataFrame, index: int = 0, distance_limit: float = 0.1) -> GeoDataFrame:
    if index < 0 or index > gdf.index.max():
        return gdf
    
    if index in gdf.index:
        END = gdf.at[index, 'end']

        gdf['distance'] = gdf['start'].apply(lambda x: _haversine_distance(x, END))
        MIN_DISTANCE_ROWS = gdf[(gdf['distance'] < distance_limit) & (gdf['distance'] == gdf['distance'].min()) & (gdf.index != index)]
        gdf.drop('distance', axis=1, inplace=True)

        if not MIN_DISTANCE_ROWS.empty:
            MIN_DISTANCE_IDX = MIN_DISTANCE_ROWS.index[0]

            COMBINED_POINTS = _combine_points(gdf.at[index, 'geometry'], gdf.at[MIN_DISTANCE_IDX, 'geometry'])
            COMBINED_LINESTRING = converter.lng_lat_to_linestring(COMBINED_POINTS)
            COMBINED_START = COMBINED_POINTS[0]
            COMBINED_END = COMBINED_POINTS[len(COMBINED_POINTS) - 1]

            gdf.at[index, 'geometry'] = COMBINED_LINESTRING
            gdf.at[index, 'start'] = COMBINED_START
            gdf.at[index, 'end'] = COMBINED_END
            
            gdf.drop(MIN_DISTANCE_IDX, axis=0, inplace=True)
    return _recursive_merge_rows(gdf, index+1, distance_limit)

def connect_gaps(gdf: GeoDataFrame, distance_limit: float = 0.1) -> GeoDataFrame:
    gdf['coordinates'] = gdf['geometry'].apply(converter.linestring_to_lng_lat)
    gdf['start'] = gdf['coordinates'].apply(lambda x: x[0])
    gdf['end'] = gdf['coordinates'].apply(lambda x: x[len(x) - 1])
    gdf.drop('coordinates', axis=1, inplace=True)

    gdf = _recursive_merge_rows(gdf, 0, distance_limit)

    gdf.drop('start', axis=1, inplace=True)
    gdf.drop('end', axis=1, inplace=True)

    return gdf