import geopandas
from geopandas import GeoDataFrame

def read_file(file: str) -> GeoDataFrame:
    """
    Lê um arquivo nos formatos KML, JSON ou Shapefile e o converte para o formato GeoDataFrame.

    :param str file: O caminho do arquivo a ser lido.
    :return gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    """
    return geopandas.read_file(file)

def write_shapefile(gdf: GeoDataFrame, filename: str = "out/file.shp.zip") -> None:
    """
    Exporta um GeoDataFrame para o formato Shapefile.

    :param GeoDataFrame gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :param str filename: O caminho do arquivo a ser exportado.
    """
    gdf.to_file(filename, driver='ESRI Shapefile')

def write_geojson(gdf: GeoDataFrame, filename: str = "out/file.geojson") -> None:
    """
    Exporta um GeoDataFrame para o formato GeoJSON.

    :param GeoDataFrame gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :param str filename: O caminho do arquivo a ser exportado.
    """
    gdf.to_file(filename, driver="GeoJSON")  