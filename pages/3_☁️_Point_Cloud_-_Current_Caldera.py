import streamlit as st
import streamlit.components.v1 as components

st.write("# Current Crater Point Cloud")

components.iframe("https://vesuvius-panoramas.s3.eu-central-1.amazonaws.com/VesuvioCrater/index.html", 
                  height=800)