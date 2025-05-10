import streamlit as st

st.title("BMI CALCULATOR")

height = st.slider("Enter Your Height (in cm): ", 1, 250)
weight = st.slider("Enter Your Weight (in kg):", 1, 150)

BMI = weight / ((height/100) ** 2)

st.write(f"Your BMI is: {BMI:.2f}")


st.write("THANKS FOR USING THIS BMI CALCULATOR")