import folium
import streamlit as st
from streamlit_folium import st_folium
import folium

st.write("# Vesuvius Gigapixels")

st.write("Use the slider below to explore the 30 panoramas. "
         "The slider is in reverse order to represent space, "
         "30 was the western-most panorama, and 1 was the eastern-most.")

gigapixel_number = st.select_slider(
    label="Select Gigapixel",
    options=[abs(x) for x in range(-30, 0)],
)

# background_html = "<style> .leaflet-container {background-color: #000000 !important;}</style>"

t = folium.TileLayer(tiles=f"http://192.168.178.129:8000/group-{gigapixel_number}-dzsl_files/{{z}}/{{x}}/{{y}}.png", 
                     max_zoom=9,
                     tms=True, 
                     attr="© 2024 Garrett Speed", 
                     no_wrap=True)


m = folium.Map(location=[0,0],
               zoom_start=5,
               tiles=t, 
               )
m.add_css_link("css", "http://192.168.178.129:8000/extraleaflet.css")

st_map = st_folium(m, 
                #    width="100%", 
                   use_container_width=True,
                   )