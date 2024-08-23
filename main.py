from lib import file_handler

gdf = file_handler.read_file("samples/lines/retas_fragmentadas.shp")
print(gdf)
file_handler.write_file(gdf)