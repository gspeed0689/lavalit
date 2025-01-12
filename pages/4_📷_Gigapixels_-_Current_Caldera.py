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
panodict = {
'group-01':{'xctr': -14.0625, 'yctr': -65.36683689226321, 'zoom': 2},
'group-02':{'xctr': -15.46875, 'yctr': -71.52490903732816, 'zoom': 2},
'group-03':{'xctr': -88.59375, 'yctr': -78.56048828398782, 'zoom': 2},
'group-04':{'xctr': -4.921875, 'yctr': -60.064840460104506, 'zoom': 2},
'group-05':{'xctr': -16.875, 'yctr': -65.36683689226321, 'zoom': 2},
'group-06':{'xctr': -86.484375, 'yctr': -67.33986082559096, 'zoom': 2},
'group-07':{'xctr': -3.515625, 'yctr': -63.54855223203643, 'zoom': 2},
'group-08':{'xctr': -23.203125, 'yctr': -64.47279382008166, 'zoom': 2},
'group-09':{'xctr': -7.734375, 'yctr': -72.18180355624852, 'zoom': 2},
'group-10':{'xctr': -27.421875, 'yctr': -74.01954331150226, 'zoom': 2},
'group-11':{'xctr': -3.515625, 'yctr': -64.16810689799152, 'zoom': 2},
'group-12':{'xctr': -33.75, 'yctr': -66.79190947341796, 'zoom': 2},
'group-13':{'xctr': -83.671875, 'yctr': -78.34941069014627, 'zoom': 2},
'group-14':{'xctr': -4.921875, 'yctr': -65.07213008560696, 'zoom': 2},
'group-15':{'xctr': -49.21875, 'yctr': -66.79190947341796, 'zoom': 2},
'group-16':{'xctr': -85.078125, 'yctr': -77.61770905279674, 'zoom': 2},
'group-17':{'xctr': -88.59375, 'yctr': -79.68718415450823, 'zoom': 2},
'group-18':{'xctr': -87.890625, 'yctr': -79.43237075914709, 'zoom': 2},
'group-19':{'xctr': -82.96875, 'yctr': -81.09321385260839, 'zoom': 2},
'group-20':{'xctr': -88.59375, 'yctr': -79.81230226556366, 'zoom': 2},
'group-21':{'xctr': -76.640625, 'yctr': -79.3026396205366, 'zoom': 2},
'group-22':{'xctr': -24.609375, 'yctr': -66.23145747862573, 'zoom': 2},
'group-23':{'xctr': -78.75, 'yctr': -79.93591824625466, 'zoom': 2},
'group-24':{'xctr': -83.671875, 'yctr': -79.68718415450823, 'zoom': 2},
'group-25':{'xctr': -73.828125, 'yctr': -79.3026396205366, 'zoom': 2},
'group-26':{'xctr': -87.1875, 'yctr': -77.46602847687328, 'zoom': 2},
'group-27':{'xctr': -75.9375, 'yctr': -76.67978490310692, 'zoom': 2},
'group-28':{'xctr': -81.5625, 'yctr': -76.67978490310692, 'zoom': 2},
'group-29':{'xctr': -79.453125, 'yctr': -76.18499546094715, 'zoom': 2},
'group-30':{'xctr': -7.03125, 'yctr': -60.239811169998916, 'zoom': 2},
}

group_num = f"group-{gigapixel_number:02d}"
group_loc = panodict[group_num]
group_loc = [group_loc["yctr"], group_loc["xctr"]] # these appear to be reversed
# st.write(str(group_loc))

t = folium.TileLayer(tiles=f"https://vesuvius-panoramas.s3.eu-central-1.amazonaws.com/{group_num}/{{z}}/{{x}}/{{y}}.webp", 
                     max_zoom=8,
                     tms=True, 
                     attr="© 2024 Garrett Speed", 
                     no_wrap=True)



m = folium.Map(location=group_loc,
               zoom_start=2,
               tiles=t, 
               max_zoom=9
               )

# p = folium.Marker(location=group_loc).add_to(m)

m.add_css_link("css", "https://vesuvius-panoramas.s3.eu-central-1.amazonaws.com/extraleaflet.css")

st_map = st_folium(m, 
                   use_container_width=True,
                   )