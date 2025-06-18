import streamlit as st
import pandas as pd
import altair as alt

# Load dataset
data = pd.read_csv("preprocessed_dataset.csv")

# Ganti nama kolom jika masih bernama 'Produksi'
if 'Produksi' in data.columns:
    data = data.rename(columns={'Produksi': 'Produksi Beras (ton)'})

# Cek apakah kolom yang dibutuhkan tersedia
if 'Tahun' in data.columns and 'Produksi Beras (ton)' in data.columns:

    st.markdown("<h1 style='font-size: 32px; color: #2E86C1;'>Data Produksi Beras Kabupaten Minahasa per Tahun</h1>", unsafe_allow_html=True)

    st.markdown("<p style='font-size: 16px; color: #333333;'>Sumber data berdasarkan rekap tahunan produksi beras dari tahun 2003 hingga 2023</p>", unsafe_allow_html=True)

    # Tampilkan data
    st.write("📊 Data Produksi Beras:")
    st.dataframe(data)

    # Chart garis
    line_chart = alt.Chart(data).mark_line(
        point=alt.OverlayMarkDef(color='#2E86C1', filled=True, size=100),
        color='#2E86C1',
        strokeWidth=3
    ).encode(
        x=alt.X('Tahun:O', title='Tahun'),
        y=alt.Y('Produksi Beras (ton):Q', title='Produksi Beras (ton)'),
        tooltip=['Tahun', 'Produksi Beras (ton)']
    ).properties(
        width=700,
        height=450,
        title=alt.TitleParams(
            text='Grafik Produksi Beras per Tahun',
            fontSize=22,
            color='#2E86C1'
        )
    )

    # Label di atas titik
    labels = alt.Chart(data).mark_text(
        align='center',
        dy=-12,
        fontSize=9,
        fontWeight='bold',
        color='#2E86C1'
    ).encode(
        x='Tahun:O',
        y='Produksi Beras (ton):Q',
        text='Produksi Beras (ton):Q'
    )

    # Gabungkan grafik
    final_chart = (line_chart + labels).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=20,
        anchor='start'
    )

    # Tampilkan chart
    st.altair_chart(final_chart, use_container_width=True)

else:
    st.error("Dataset tidak memiliki kolom 'Tahun' dan 'Produksi Beras (ton)'. Harap periksa struktur dataset.")
