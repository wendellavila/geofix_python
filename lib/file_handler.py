import geopandas
from geopandas import GeoDataFrame

def read_file(file: str) -> GeoDataFrame:
    return geopandas.read_file(file)

def write_file(gdf: GeoDataFrame, filename: str = "out/file.shp.zip") -> None:
    gdf.to_file(filename, driver='ESRI Shapefile')

def write_file2(gdf: GeoDataFrame, filename: str = "out/file.geojson") -> None:
    gdf.to_file(filename, driver="GeoJSON")  