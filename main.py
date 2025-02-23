import streamlit as st

# Title of the App
st.title("Streamlit 3-Page Project")

# Add a selectbox to choose between pages
page = st.sidebar.selectbox("Choose a page", ["Home", "Page 1", "Page 2", "Page 3"])

if page == "Home":
    st.header("Welcome to the Home Page!")
    st.write("This is the landing page of your Streamlit app.")
elif page == "Page 1":
    st.header("Welcome to Page 1")
    st.write("This is the first page of the app. You can add any content here!")
elif page == "Page 2":
    st.header("Welcome to Page 2")
    st.write("This is the second page. You can display charts, images, and more.")
    
elif page == "Page 3":
    st.header("Welcome to Page 3")
    st.write("This is the third page. Display more content here or add another feature!")
