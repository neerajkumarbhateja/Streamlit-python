
import streamlit as st

# Page 3 Content
st.title("Page 3")
st.write("This page can include more advanced content, like machine learning models or statistics.")

# Example: Displaying an interactive map
import folium
from streamlit_folium import st_folium

map_center = [37.7749, -122.4194]  # Coordinates for San Francisco
my_map = folium.Map(location=map_center, zoom_start=12)

# Display the map on Streamlit
st_folium(my_map, width=700, height=500)
