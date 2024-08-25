from lib import file_handler
from lib import converter
from lib import connector

gdf = file_handler.read_file("samples/curves/arcos_fragmentados.shp")

gdf = converter.coordinates_to_wgs84(gdf)
gdf = converter.split_multipart(gdf)
gdf = connector.connect_gaps(gdf, distance_limit=0.05)
gdf = connector.connect_gaps(gdf, distance_limit=0.08)

file_handler.write_file2(gdf, 'out/file2pre.geojson')