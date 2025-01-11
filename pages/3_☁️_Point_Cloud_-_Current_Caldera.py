import streamlit as st
import streamlit.components.v1 as components

st.write("# Current Crater Point Cloud")

components.iframe("http://localhost:8000/VesuvioCrater/", 
                  height=600)