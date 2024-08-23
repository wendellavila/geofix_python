from geopandas import GeoDataFrame

def to_wgs84(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf.to_crs(epsg=4326)

def to_line_string(gdf: GeoDataFrame) -> GeoDataFrame:
    return gdf.explode()