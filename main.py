from lib import file_handler
from lib import converter
from lib import connector

gdf = file_handler.read_file("samples/lines/retas_fragmentadas.shp")
gdf = converter.to_wgs84(gdf)
gdf = converter.to_line_string(gdf)

line_string = gdf.at[0, 'geometry']
print(connector.line_string_to_points(line_string))

# print(gdf)
# file_handler.write_file(gdf)