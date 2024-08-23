from lib import file_handler
from lib import converter

gdf = file_handler.read_file("samples/lines/retas_fragmentadas.shp")
gdf = converter.coordinates_to_wgs84(gdf)
gdf = converter.split_multipart(gdf)

line_string = gdf.at[0, 'geometry']
print(converter.line_string_to_points(line_string))

# print(gdf)
# file_handler.write_file(gdf)