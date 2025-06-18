import pickle
import streamlit as st

# Load the model
model = pickle.load(open('model_linear_regression.pkl', 'rb'))

# Custom CSS
st.markdown("""
    <style>
    /* Header dan subjudul */
    h1 {
        font-size: 36px;
        color: #2E86C1;
        margin-bottom: 5px;
    }

    p {
        font-size: 18px;
        color: #333333;
        margin-top: 0;
    }

    /* Input dan label */
    .stNumberInput {
        margin-top: -10px;
    }
    label, .stNumberInput input {
        font-size: 18px !important;
    }

    /* Tombol */
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Judul dan deskripsi
st.markdown("<h1>Dashboard Prediksi Produksi Beras Kabupaten Minahasa</h1>", unsafe_allow_html=True)

# Input pengguna (tanpa jarak label dan input)
st.markdown("<p style='font-size:18px; font-weight:bold; margin-bottom:0;'>Input Luas Panen (Ha)</p>", unsafe_allow_html=True)
luas_panen = st.number_input('', key='luas')

st.markdown("<p style='font-size:18px; font-weight:bold; margin-bottom:0;'>Input Curah Hujan (mm)</p>", unsafe_allow_html=True)
curah_hujan = st.number_input('', key='curah')

st.markdown("<p style='font-size:18px; font-weight:bold; margin-bottom:0;'>Input Hari Hujan (Hari)</p>", unsafe_allow_html=True)
hari_hujan = st.number_input('', key='hari')

st.markdown("<p style='font-size:18px; font-weight:bold; margin-bottom:0;'>Input Suhu (°C)</p>", unsafe_allow_html=True)
suhu = st.number_input('', key='suhu')

st.markdown("<p style='font-size:18px; font-weight:bold; margin-bottom:0;'>Input Kelembapan Udara (%)</p>", unsafe_allow_html=True)
kelembapan_udara = st.number_input('', key='lembap')

# Tombol prediksi dan output
predict = ''
if st.button('Prediksi'):
    predict = model.predict(
        [[luas_panen, curah_hujan, hari_hujan, suhu, kelembapan_udara]]
    )
    st.write('#### Prediksi Jumlah Produksi Beras (Ton): ', float(predict[0]),)
