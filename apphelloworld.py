import streamlit as st

st.set_page_config(page_title="Dashboard Hello World", layout="wide")

# Sidebar navigasi manual
st.sidebar.title("Menu")
page = st.sidebar.radio("Pilih Halaman:", ["Home", "Predict Hello", "Record Hello", "Data Hello"])

if page == "Home":
    st.title("Hello World Dashboard - Home")
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Visualisasi Contoh")
        st.bar_chart([2, 4, 6, 8])
    with col2:
        st.subheader("Detail Informasi")
        st.markdown("""
        - Predict Hello: Prediksi sederhana dari input nama.
        - Record Hello: Simpan pesan Hello.
        - Data Hello: Tampilkan data Hello World.
        """)

elif page == "Predict Hello":
    st.title("Predict Hello")
    name = st.text_input("Masukkan nama kamu:")
    if name:
        st.success(f"Halo, {name}! Ini adalah prediksi Hello World untukmu.")

elif page == "Record Hello":
    st.title("Record Hello")
    text = st.text_area("Tulis pesan Hello kamu di sini:")
    if st.button("Simpan"):
        st.info("Pesan telah disimpan (simulasi).")

elif page == "Data Hello":
    st.title("Data Hello")
    import pandas as pd
    data = pd.DataFrame({
        'Nama': ['Alice', 'Bob', 'Charlie'],
        'Pesan': ['Hello!', 'Hi there!', 'Howdy!']
    })
    st.dataframe(data)
