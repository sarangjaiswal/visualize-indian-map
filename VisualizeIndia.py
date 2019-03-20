# import library
import geopandas as gpd
import os
import folium

# get current directory path
cur_dir = os.path.dirname(os.path.realpath(__file__))

df_shp_india = gpd.read_file(cur_dir + '/data/IndiaBoundary/IndiaBoundary.shp')
df_shp_state = gpd.read_file(cur_dir + '/data/StateBoundary/StateBoundary.shp')
df_gpkg = gpd.read_file(cur_dir + '/data/gadm36_IND_gpkg/gadm36_IND.gpkg')


print(df_shp_state.query())

# Open the map at a location with a certain zoom start
# http://geojson.io/#map=5/22.573/74.751
m = folium.Map(location=[22.573, 74.751], zoom_start=5)

# plot all
folium.GeoJson(df_shp_state).add_to(m)

# plot top 10 states
# folium.GeoJson(df_shp_state.head(10)).add_to(m)

# plot by query
# folium.GeoJson(df_shp_state.query().add_to(m)

m.save('map.html')
