import pickle
import streamlit as st

# Load the model
model = pickle.load(open('model_linear_regression.pkl', 'rb'))

st.title('Prediksi Produksi Beras Kabupaten Minahasa')
st.write('Prediksi produksi beras berdasarkan data tahunan dari tahun 2003-2023')

luas_panen = st.number_input('Input Luas Panen (Ha)')
curah_hujan = st.number_input('Input Curah Hujan (mm)')
hari_hujan = st.number_input('Input Hari Hujan (Hari)')
suhu = st.number_input('Input Suhu (°C)')
kelembapan_udara = st.number_input('Input Kelembapan Udara (%)')

predict = ''

# Custom CSS untuk tombol prediksi
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Warna hijau */
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #45a049; /* Warna hijau lebih gelap saat hover */
    }
    </style>
    """, unsafe_allow_html=True)

if st.button('Prediksi'):
    predict = model.predict(
        [[luas_panen, curah_hujan, hari_hujan, suhu, kelembapan_udara]]
        )
    st.write('Prediksi Jumlah Produksi Beras (Ton): ', predict)