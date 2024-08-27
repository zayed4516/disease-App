import streamlit as st
import pickle
import os

# Check if the model file exists
if not os.path.isfile('disease.pkl'):
    st.error("The model file 'disease.pkl' is not found in the specified path.")
    st.stop()

# Load the model
with open('disease.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the page
st.title("Diabetes Prediction")

# Input fields
Pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0)
Glucose = st.number_input('Glucose', min_value=0, max_value=300, value=100)
BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=200, value=70)
SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
Insulin = st.number_input('Insulin', min_value=0, max_value=1000, value=80)
BMI = st.number_input('BMI', min_value=0.0, max_value=60.0, value=25.0)
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5)
Age = st.number_input('Age', min_value=0, max_value=120, value=30)

# Prediction
if st.button('Predict'):
    input_features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    prediction = model.predict(input_features)
    
    # Display the result
    result = "Diabetes likely" if prediction[0] == 1 else "No diabetes"
    st.write(f"Prediction: {result}")

