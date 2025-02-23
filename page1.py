import streamlit as st

# Page 1 Content
st.title("Page 1")
st.write("This page can contain information, data, or visualizations related to topic 1.")

# Example: Display a simple plot or image
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
st.pyplot(plt)
