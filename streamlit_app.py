
import streamlit as st
import pickle

# load pkl file
with open('disease.pkl', 'rb') as file:
    model = pickle.load(file)

#title the page
st.title("predict diabetes")


#inputs
Pregnancies = st.number_input('Pregnancies' , min_value=0.0 , max_value=10.0,value=.01)
Glucose = st.number_input('Glucose' , min_value=0.0 , max_value=10.0,value=.01)
BloodPressure = st.number_input('BloodPressure' , min_value=0.0 , max_value=100.0,value=0.01)
SkinThickness = st.number_input('SkinThickness' , min_value=0.0 , max_value=100.0,value=0.01)
Insulin =  st.number_input('Insulin' , min_value=0.0 , max_value=100.0,value=.01)
BMI =  st.number_input('BMI' , min_value=0.0 , max_value=100.0,value=.01)
DiabetesPedigreeFunction =  st.number_input('DiabetesPedigreeFunction' , min_value=0.0 , max_value=100.0,value=.01)
Age =  st.number_input('Age' , min_value=0.0 , max_value=100.0,value=.01)


output = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

#display the result
st.write("the predict diabetes : ",output[0])
