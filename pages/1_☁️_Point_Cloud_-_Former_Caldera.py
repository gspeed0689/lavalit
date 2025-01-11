import streamlit as st
import streamlit.components.v1 as components

st.write("# Former Caldera Point Cloud")

components.iframe("http://192.168.178.129:8000/OldCaldera/", 
                  height=600)