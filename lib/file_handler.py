# imports
# biblioteca padrão
import os
# dependências
import geopandas
from geopandas import GeoDataFrame

def read_file(file: str) -> GeoDataFrame:
    """
    Lê um arquivo nos formatos KML, JSON ou Shapefile e o converte para o formato GeoDataFrame.

    :param str file: O caminho do arquivo a ser lido.
    :return gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :raises FileNotFoundError: Arquivo não existe no caminho fornecido.
    :raises ValueError: Extensão de arquivo não suportada.
    """
    if not os.path.isfile(file):
        raise FileNotFoundError()
    
    ext = os.path.splitext(file)[-1].lower()
    if ext not in ('.json', '.geojson' ,'.kml', '.shp', '.zip'):
        raise ValueError()

    return geopandas.read_file(file)

def write_shapefile(gdf: GeoDataFrame, filename: str) -> None:
    """
    Exporta um GeoDataFrame para o formato Shapefile.

    :param GeoDataFrame gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :param str filename: O caminho do arquivo a ser exportado.
    """
    dir = os.path.dirname(filename)
    if not os.path.isdir(dir):
        raise FileNotFoundError()
    gdf.to_file(filename, driver='ESRI Shapefile')

def write_geojson(gdf: GeoDataFrame, filename: str) -> None:
    """
    Exporta um GeoDataFrame para o formato GeoJSON.

    :param GeoDataFrame gdf: Um GeoDataFrame criado pela biblioteca geopandas.
    :param str filename: O caminho do arquivo a ser exportado.
    :raises FileNotFoundError: Diretório do caminho de saída fornecido não existe.
    """
    dir = os.path.dirname(filename)
    if not os.path.isdir(dir):
        raise FileNotFoundError()
    gdf.to_file(filename, driver="GeoJSON")

def strip_extension(filename: str) -> str:
    return os.path.splitext(filename)[0]