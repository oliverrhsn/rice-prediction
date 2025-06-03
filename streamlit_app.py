import streamlit as st


# --- PAGE SETUP ---
prediction_page = st.Page(
    "views/prediction.py",
    title="Dashboard Prediksi",
    icon=":material/monitoring:",
    default=True,
)
chart_page = st.Page(
    "views/chart.py",
    title="Dataset & Chart",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[prediction_page, chart_page])

# --- SHARED ON ALL PAGES ---
st.logo("assets/logo_prediksi.png")
st.sidebar.markdown("Made by [Oliver](https://www.linkedin.com/in/oliverrhsn)")

# --- RUN NAVIGATION ---
pg.run()