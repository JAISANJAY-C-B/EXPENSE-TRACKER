import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expense Tracker")

uploaded_file = st.file_uploader("Upload Expense File", type=["csv","xlsx"])

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Preview")
    st.dataframe(df)

    if st.button("Analyze"):

        st.write("Total Spend:", df['amount'].sum())

        st.write("Category Wise Spend")
        st.write(df.groupby('category')['amount'].sum())

        # Pie Chart
        fig1, ax1 = plt.subplots()
        df.groupby('category')['amount'].sum().plot.pie(autopct='%1.1f%%', ax=ax1)
        st.pyplot(fig1)

        # Line Chart
        fig2, ax2 = plt.subplots()
        df.groupby('date')['amount'].sum().plot(ax=ax2)
        st.pyplot(fig2)
