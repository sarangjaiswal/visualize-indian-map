# import library
import geopandas as gpd
import os
import folium

# get current directory path
cur_dir = os.path.dirname(os.path.realpath(__file__))

# target path to save map
map_path = cur_dir + '/maps/indian_state_boundary_map.html'

# reading shape files with geopandas
gdf_shp_state = gpd.read_file(cur_dir + '/data/StateBoundary/StateBoundary.shp')

# Open the map at a location with a certain zoom start - http://geojson.io/#map=5/22.573/74.751
m = folium.Map(location=[22.573, 74.751], zoom_start=5)

# querying the geopandas for a state
gdf_shp_maharashtra = gdf_shp_state.query("state=='MAHARASHTRA'")

# below are few other ways you can query in geopandas
# print(gdf_shp_state.loc[gdf_shp_state.state == 'MAHARASHTRA'])
# print(gdf_shp_state[gdf_shp_state.state == 'MAHARASHTRA'])

# convert the geopandas data to geojson and add to map
folium.GeoJson(gdf_shp_maharashtra).add_to(m)

#  convert the geopandas data to geojson and add to map
# folium.GeoJson(gdf_shp_state).add_to(m)

# save map
m.save(map_path)
