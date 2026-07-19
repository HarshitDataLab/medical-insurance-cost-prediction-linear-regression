import streamlit as st
import numpy as np
import pickle

# Load model
loaded_model = pickle.load(open('Medical_Insurance_Cost_Prediction.sav', 'rb'))

st.set_page_config(page_title="Medical Insurance Cost Prediction")

st.title("🏥 Medical Insurance Cost Prediction")

# Input fields
age = st.number_input("Age", 18, 100, 25)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

bmi = st.number_input("BMI", value=25.0)

children = st.number_input("Children", 0, 10, 0)

smoker = st.selectbox("Smoker", ["No", "Yes"])
smoker = 1 if smoker == "Yes" else 0

region = st.selectbox(
    "Region",
    ["Southwest", "Southeast", "Northwest", "Northeast"]
)

region_dict = {
    "Southwest": 0,
    "Southeast": 1,
    "Northwest": 2,
    "Northeast": 3
}

region = region_dict[region]

if st.button("Predict Insurance Cost"):

    input_data = np.array([[
        age,
        sex,
        bmi,
        children,
        smoker,
        region
    ]])

    prediction = loaded_model.predict(input_data)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")