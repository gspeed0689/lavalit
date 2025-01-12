import folium
import streamlit as st
from streamlit_folium import st_folium
import folium

st.write("# Monte di Procida Panoramas")

st.write("Northwest of Vesuvius is a small town known as Monte di Procida, named for its closeness to the island Procida. "
         "The day before we hiked Vesuvius we were in the town's harbor, and across from the harbor is a beach and cliff face with beautiful stratigraphy. "
         "Most of the rock is yellow, so probably tufo, but in this series you can see a grey section probably from an eruption.")

gigapixel_number = st.select_slider(
    label="Select Gigapixel - 14 is the western-most and 1 is the eastern-most. ",
    options=[abs(x) for x in range(-14, 0)],
)

panodict = {
'mdp-group-01':{'xctr': -53.4375, 'yctr': -80.17871349622823, 'zoom': 2},
'mdp-group-02':{'xctr': -36.5625, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-03':{'xctr': -45.0, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-04':{'xctr': -42.1875, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-05':{'xctr': -25.3125, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-06':{'xctr': -30.9375, 'yctr': -80.17871349622823, 'zoom': 2},
'mdp-group-07':{'xctr': -28.125, 'yctr': -79.17133464081945, 'zoom': 2},
'mdp-group-08':{'xctr': -42.1875, 'yctr': -79.17133464081945, 'zoom': 2},
'mdp-group-09':{'xctr': -28.125, 'yctr': -80.17871349622823, 'zoom': 2},
'mdp-group-10':{'xctr': -11.25, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-11':{'xctr': -19.6875, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-12':{'xctr': -16.875, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-13':{'xctr': -19.6875, 'yctr': -79.68718415450823, 'zoom': 2},
'mdp-group-14':{'xctr': -8.4375, 'yctr': -79.68718415450823, 'zoom': 2},


}

group_num = f"mdp-group-{gigapixel_number:02d}"
group_loc = panodict[group_num]
group_loc = [group_loc["yctr"], group_loc["xctr"]] # these appear to be reversed
# st.write(str(group_loc))

t = folium.TileLayer(tiles=f"https://vesuvius-panoramas.s3.eu-central-1.amazonaws.com/{group_num}/{{z}}/{{x}}/{{y}}.webp", 
                     max_zoom=7,
                     tms=True, 
                     attr="© 2024 Garrett Speed", 
                     no_wrap=True)


m = folium.Map(location=group_loc,
               zoom_start=3,
               tiles=t, 
               max_zoom=8
               )
m.add_css_link("css", "https://vesuvius-panoramas.s3.eu-central-1.amazonaws.com/extraleaflet.css")

st_map = st_folium(m, 
                   use_container_width=True,
                   )