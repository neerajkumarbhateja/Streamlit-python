import streamlit as st

# Page 2 Content
st.title("Page 2")
st.write("Here you can showcase other types of data or features, like interactive visualizations.")

# Example: Display a simple dataframe
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 35, 45],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
st.dataframe(df)
