import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV", type=["xlsx", "xls"])

if uploaded_file is not None:
    st.write("File Uploaded..")
    df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("select column", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select value", unique_values)

    filetered_df = df[df[selected_columns] == selected_values]
    st.write(filetered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("select x_axis", columns)
    y_column = st.selectbox("select y_axis", columns)

    if st.button("Generate Plot"):
        st.line_chart(filetered_df.set_index(x_column)[y_column])
else:
    st.write("Thanks For Using Our Dashboard")