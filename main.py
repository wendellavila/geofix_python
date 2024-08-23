from lib import file_handler
from lib import converter

gdf = file_handler.read_file("samples/lines/retas_fragmentadas.shp")
gdf = converter.to_wgs84(gdf)
gdf = converter.to_line_string(gdf)

print(gdf)

file_handler.write_file(gdf)