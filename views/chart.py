import streamlit as st
import pandas as pd
import altair as alt

# Load dataset dan ubah nama kolom 'Produksi' menjadi 'Produksi Beras (ton)'
data = pd.read_csv("preprocessed_dataset.csv")
#data = data.rename(columns={'Produksi': 'Produksi Beras (ton)'})

# Pastikan kolom yang diperlukan ada
if 'Tahun' in data.columns and 'Produksi Beras (ton)' in data.columns:
    # Menampilkan judul
    st.title("Data Produksi Beras Kabupaten Minahasa per Tahun")

    # Menampilkan dataset (opsional)
    st.write("Data Produksi Beras:")
    st.dataframe(data)

    # Membuat line chart dengan Altair
    line_chart = alt.Chart(data).mark_line(point=True).encode(
        x='Tahun:O',
        y='Produksi Beras (ton):Q',
        tooltip=['Tahun', 'Produksi Beras (ton)']
    ).properties(
        width=700,
        height=600,
        title="Line Chart Jumlah Produksi Beras per Tahun"
    )

    # Menambahkan label pada setiap titik dengan ukuran font lebih kecil
    labels = alt.Chart(data).mark_text(
        align='left',
        dx=5,
        dy=-10,
        color='white',
        size=7  # Mengatur ukuran font label menjadi lebih kecil
    ).encode(
        x='Tahun:O',
        y='Produksi Beras (ton):Q',
        text='Produksi Beras (ton):Q'
    )

    # Menggabungkan grafik garis dan label
    chart = line_chart + labels

    # Menampilkan chart di Streamlit
    st.altair_chart(chart, use_container_width=True)
else:
    st.error("Dataset tidak memiliki kolom 'Tahun' dan 'Produksi Beras (ton)'. Harap cek format dataset.")
