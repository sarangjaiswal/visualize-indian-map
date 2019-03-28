# import library
import geopandas as gpd
import os
import folium
import pandas as pd
import json

# get current directory path
cur_dir = os.path.dirname(os.path.realpath(__file__))

# target path to save map
map_path = cur_dir + '/maps/color_indian_state_boundary_map.html'

# reading shape files with geopandas
gdf = gpd.read_file(cur_dir + '/data/StateBoundary/StateBoundary.shp')
df = pd.read_csv(cur_dir + '/data/state_color.csv')
state_geo = json.load(open(os.path.join('data', 'state.json')))


# Open the map at a location with a certain zoom start - http://geojson.io/#map=5/22.573/74.751
m = folium.Map(location=[22.573, 74.751], zoom_start=5)

folium.Choropleth(
    geo_data=gdf.query("state=='MAHARASHTRA'"),
    fill_color='Yellow',
    fill_opacity=0.5,
    line_color='blue',
    line_weight=1,
    line_opacity=1,
    highlight=True
).add_to(m)

folium.Choropleth(
    geo_data=gdf.query("state=='GUJARAT'"),
    fill_color='Blue',
    fill_opacity=0.5,
    line_color='blue',
    line_weight=1,
    line_opacity=1,
    highlight=True
).add_to(m)

# save map
m.save(map_path)
