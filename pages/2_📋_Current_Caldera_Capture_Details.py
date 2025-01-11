import streamlit as st
from streamlit_folium import st_folium
import folium

with open("content/rim_intro.md", "r") as rim_intro_file:
    rim_intro_markdown = rim_intro_file.read()

st.markdown(rim_intro_markdown)

with open("content/details-panorama.geojson") as rim_loc_file:
    rim_loc_geojson = rim_loc_file.read()

rim_loc_map = folium.Map(location=[40.820889, 14.4246],
           zoom_start=16,
           scroll_wheel_zoom=False)

rim_loc_tooltip = folium.GeoJsonTooltip(["tooltip"], aliases=[""])

folium.GeoJson(rim_loc_geojson, 
               tooltip=rim_loc_tooltip).add_to(rim_loc_map)

rim_loc_st = st_folium(rim_loc_map,
                       use_container_width=True)