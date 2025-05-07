import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Micrometers": 1000000,
        "Nanometers": 1000000000,
        "Yards": 1.09361,
        "Nauctical meters": 0.000539957,

    }
    return value * conversions[to_unit] / conversions[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversions = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value


st.title("Unit Converter")


conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet", "Inches" , "Centimeters" , "Millimeters" , "Micrometers" , "Nanometers" , "Yards" , "Nauctical meters"]
    convert_function = length_converter
elif conversion_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    convert_function = weight_converter
else:
    units = ["Celsius", "Fahrenheit"]
    convert_function = temperature_converter


value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)


if st.button("Convert"):
    result = convert_function(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
