import streamlit as st
import streamlit.components.v1 as components

st.write("# Former Caldera Point Cloud")

components.iframe("https://vesuvius-panoramas.s3-website.eu-central-1.amazonaws.com/OldCaldera/", 
                  height=800)