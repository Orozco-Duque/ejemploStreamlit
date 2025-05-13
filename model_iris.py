import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load("random_forest_model.pkl")

# Set the title of the app
st.title("Random Forest Model Prediction")
st.write("This app predicts the target variable using a Random Forest model.")

# Create a sidebar for user input
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.5)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

# Prediction button
if st.button("Predict"):
    # Create a DataFrame with the input data
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make a prediction
    prediction = model.predict(input_data)
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    result = class_names[prediction[0]]
    # Display the prediction
    st.write(f"Predicted class: {result}")