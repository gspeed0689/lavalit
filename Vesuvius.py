import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(
    page_title="Vesuvius Panoramas and Point Cloud", 
    page_icon="🌋",
    layout="wide"
)

with open("content/intro.md", "r") as intro_file:
    intro_markdown = intro_file.read()

st.markdown(intro_markdown)

parking2caldera = folium.Map(location=[40.82119, 14.42865], 
                             zoom_start=14,
                             scroll_wheel_zoom=False)

with open("content/vesuvio-parking2cone.geojson", "r") as p2c_file:
    p2c_json = p2c_file.read()

p2c_tooltip = folium.GeoJsonTooltip(
    ["tooltip"], aliases=[""]
)
folium.GeoJson(p2c_json,
               tooltip=p2c_tooltip).add_to(parking2caldera)

st_p2c_map = st_folium(parking2caldera,
                       use_container_width=True)

with open("content/intro_mid.md", "r") as mid_file:
    mid_markdown = mid_file.read()

st.markdown(mid_markdown)

rimmap = folium.Map(location=[40.821016, 14.426154], 
                    zoom_start=17,
                    scroll_wheel_zoom=False)

with open("content/vesuvio-rim.geojson", "r") as rim_file:
    rim_json = rim_file.read()

rim_tooltip = folium.GeoJsonTooltip(
    ["tooltip"], aliases=[""]
)

folium.GeoJson(rim_json, 
               tooltip=rim_tooltip).add_to(rimmap)

rimst = st_folium(rimmap,
          use_container_width=True)