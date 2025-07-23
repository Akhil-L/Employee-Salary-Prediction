import streamlit as st
import pickle
import numpy as np

# Load model
try:
    model = pickle.load(open('best_model.pkl', 'rb'))
except Exception as e:
    st.error("Model file not found or not loaded properly.")

st.title("Employee Salary Prediction")

age = st.slider('Age', 18, 90, 30)
education_num = st.slider('Education Level (numeric)', 1, 16, 10)
hours_per_week = st.slider('Hours Worked Per Week', 1, 99, 40)
capital_gain = st.number_input('Capital Gain', 0, 99999, 0)
capital_loss = st.number_input('Capital Loss', 0, 99999, 0)

if st.button('Predict'):
    data = np.array([[age, education_num, hours_per_week, capital_gain, capital_loss]])
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.success("Prediction: Salary > 50K")
    else:
        st.info("Prediction: Salary <= 50K")
