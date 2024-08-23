from lib import file_handler
from lib import converter
from lib import connector

gdf = file_handler.read_file("samples/lines/retas_fragmentadas.shp")
gdf = converter.coordinates_to_wgs84(gdf)
gdf = converter.split_multipart(gdf)
gdf = connector.connect_gaps(gdf)

# print(gdf)
# file_handler.write_file(gdf)