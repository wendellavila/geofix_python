# imports
# biblioteca padrão
import time
import argparse
import sys
# módulo customizado
from lib import file_handler
from lib import converter
from lib import connector

parser = argparse.ArgumentParser(
    prog='geofix',
    description='Script para padronizar arquivos de linhas vetorizadas e georreferenciadas.')

parser.add_argument('file', type=str, help="Caminho para o arquivo de entrada nos formatos .json, .geojson, .kml, .shp ou .zip")
parser.add_argument('-o', '--output', type=str, help="Caminho para o arquivo de saída, no formato .zip. "+\
    "Se não for fornecido, o arquivo será salvo no diretório do arquivo de entrada.")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

file = args.file
out_path = args.output

if out_path is None:
    curr_time = time.strftime("%Y%m%d_%H%M%S")
    out_path = f"{file_handler.strip_extension(file)}_out_{curr_time}.zip"

gdf = file_handler.read_file(file)
gdf = converter.coordinates_to_wgs84(gdf)
gdf = converter.split_multipart(gdf)
gdf = connector.connect_gaps(gdf, distance_limit=0.05)
gdf = connector.connect_gaps(gdf, distance_limit=0.08)
file_handler.write_shapefile(gdf, out_path)

parser.exit()