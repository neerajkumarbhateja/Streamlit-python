import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Title of the App
st.title("Advanced Streamlit Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation Panel")
page = st.sidebar.radio("Choose a Page", ["Home", "Page 1", "Page 2", "Page 3"])

# Home Page with Dashboard
if page == "Home":
    st.header("Welcome to the Interactive Dashboard!")

    # Sidebar Filters Section
    st.sidebar.subheader("Filters")
    # Adding a slider to filter data based on values
    value_filter = st.sidebar.slider("Select Range of Values", min_value=0, max_value=100, value=(20, 80))
    
    # Adding a date range filter
    start_date, end_date = st.sidebar.date_input("Select Date Range", value=[pd.to_datetime("2022-01-01"), pd.to_datetime("2022-04-01")])
    
    # Adding a checkbox to show/hide advanced settings
    show_advanced = st.sidebar.checkbox("Show Advanced Settings")
    if show_advanced:
        st.sidebar.text("Advanced Settings enabled!")
        st.sidebar.radio("Choose a Color Scheme", ["Blue", "Green", "Red"])

    # Sample Data Creation for Charts
    dates = pd.date_range('2022-01-01', periods=100)
    values = np.random.randn(100).cumsum()
    df = pd.DataFrame({'Date': dates, 'Value': values})

    # Filter data based on slider and date range
    filtered_df = df[(df['Value'] >= value_filter[0]) & (df['Value'] <= value_filter[1])]
    filtered_df = filtered_df[(filtered_df['Date'] >= pd.to_datetime(start_date)) & (filtered_df['Date'] <= pd.to_datetime(end_date))]

    # Display filtered data
    st.subheader(f"Filtered Data (Values between {value_filter[0]} and {value_filter[1]})")
    st.write(filtered_df)

    # Line chart with filtered data
    st.subheader("Filtered Line Chart")
    st.line_chart(filtered_df.set_index('Date'))

    # Plotly Interactive Bar Chart
    st.subheader("Interactive Bar Chart")
    bar_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': np.random.randint(10, 100, 5)
    })
    bar_fig = px.bar(bar_data, x='Category', y='Value', title="Category Value Distribution")
    st.plotly_chart(bar_fig)

    # Interactive Plotly Scatter Plot with custom styling
    st.subheader("Styled Scatter Plot")
    scatter_data = pd.DataFrame({
        'X': np.random.randn(100),
        'Y': np.random.randn(100),
        'Category': np.random.choice(['A', 'B', 'C'], 100)
    })
    scatter_fig = px.scatter(scatter_data, x='X', y='Y', color='Category', size_max=15, title="Scatter Plot with Categories")
    st.plotly_chart(scatter_fig)

    # Add a dropdown menu for category selection
    category_filter = st.selectbox("Select a Category", ['A', 'B', 'C'])
    st.write(f"Displaying data for category: {category_filter}")

    # Filter and display data based on selected category
    category_data = scatter_data[scatter_data['Category'] == category_filter]
    st.write(category_data)

    # Interactive Map (Mapbox-style visualization)
    st.subheader("Interactive Geospatial Data")
    geo_data = pd.DataFrame({
        'lat': np.random.uniform(low=40, high=42, size=100),
        'lon': np.random.uniform(low=-75, high=-73, size=100),
        'size': np.random.randint(10, 100, 100),
    })

    map_fig = px.scatter_geo(geo_data, lat='lat', lon='lon', size='size', title="Random Geospatial Data", template="plotly")
    st.plotly_chart(map_fig)

    # Button to show extra content
    if st.button('Click me to reveal more data!'):
        st.write("Here's some extra content, you clicked the button!")

elif page == "Page 1":
    st.header("Welcome to Page 1")
    st.write("This is the first page of the app. You can add any content here!")

elif page == "Page 2":
    st.header("Welcome to Page 2")
    st.write("This is the second page. You can display charts, images, and more.")

elif page == "Page 3":
    st.header("Welcome to Page 3")
    st.write("This is the third page. Display more content here or add another feature!")
