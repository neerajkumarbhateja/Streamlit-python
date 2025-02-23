import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Page 1 Content
st.title("Page 1")
st.write("This page contains information, data, and visualizations related to Topic 1.")

# Example: Display a simple plot or image
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotting the sine waveP
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X values")
plt.ylabel("Y values")
st.pyplot(plt)

# Linear Regression Section
st.subheader("Linear Regression Example")

# Generate sample data for linear regression
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Feature
y = 2 * X + np.random.randn(100, 1) * 2  # Target variable with noise

# Create the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', linewidth=2, label='Linear regression line')
plt.title("Linear Regression: Data vs Prediction")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
st.pyplot(plt)

# Display model coefficients
st.write(f"Linear Regression Coefficients: {model.coef_}")
st.write(f"Linear Regression Intercept: {model.intercept_}")

# Excel File Upload Section
st.subheader("Upload Excel File and View Data")

# Uploading the Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xls", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file)
    
    # Display the first few rows of the DataFrame
    st.write("Here is the data from your uploaded Excel file:")
    st.dataframe(df)

    # Optional: Display some basic statistics or info
    st.write("Basic Information of the Data:")
    st.write(df.describe())

    # Optionally, allow the user to download the data again as a CSV
    st.download_button(
        label="Download Data as CSV",
        data=df.to_csv(index=False),
        file_name="uploaded_data.csv",
        mime="text/csv"
    )

