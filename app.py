import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="🏥"
)

st.title("🏥 Medical Insurance Cost Prediction")
st.write("Enter the details below to estimate medical insurance cost.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)

sex = st.selectbox("Sex", ["male", "female"])

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.selectbox("Smoker", ["yes", "no"])

region = st.selectbox(
    "Region",
    ["southeast", "southwest", "northeast", "northwest"]
)

# Encoding same as notebook
sex_map = {
    "male": 0,
    "female": 1
}

smoker_map = {
    "yes": 1,
    "no": 0
}

region_map = {
    "southeast": 0,
    "southwest": 1,
    "northeast": 2,
    "northwest": 3
}

input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex_map[sex]],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker_map[smoker]],
    "region": [region_map[region]]
})

if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")