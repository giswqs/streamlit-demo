import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector data")

    m = leafmap.Map(center=[0, 0], zoom=2)

    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")

    m.to_streamlit(height=700)
