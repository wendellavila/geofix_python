from geopandas import GeoDataFrame

def has_lines(gdf: GeoDataFrame) -> bool:
    return False

def connect_lines(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf

def connect_curves(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf

def connect_gaps(gdf: GeoDataFrame) -> GeoDataFrame:
    return connect_lines(gdf) if has_lines(gdf) else connect_curves(gdf) 