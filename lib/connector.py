from geopandas import GeoDataFrame
from lib import converter

def connect_gaps(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf