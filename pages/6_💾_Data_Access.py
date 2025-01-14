import streamlit as st

with open("content/data_intro.md") as data_intro_file:
    data_intro_markdown = data_intro_file.read()

st.markdown(data_intro_markdown)

st.link_button("Zenodo 10.5281/zenodo.14634096", "https://doi.org/10.5281/zenodo.14634096")