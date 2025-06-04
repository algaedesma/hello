import streamlit as st

st.set_page_config(page_title="Hello World App", layout="wide")

st.title("Hello World App")
st.write("Aplikasi ini menunjukkan contoh multi-halaman dengan Streamlit.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Visualisasi Contoh")
    st.bar_chart([2, 4, 6, 8])

with col2:
    st.subheader("Detail Informasi")
    st.markdown("""
    **1. Halaman Predict Hello**  
    Ini adalah halaman untuk menampilkan prediksi berdasarkan input sederhana.

    **2. Halaman Record Hello**  
    Kamu bisa mencatat data 'Hello' di sini.

    **3. Halaman Data Hello**  
    Menampilkan data yang berkaitan dengan Hello World.
    """)
