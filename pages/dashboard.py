import streamlit as st
from components.cards.metric_card import metric_card
from services.service_container import services

st.title("Dashboard")
stats=services.dashboard.get_statistics()
c1,c2,c3=st.columns(3)
with c1: metric_card("Total Anak",stats["total_patient"])
with c2: metric_card("Pengukuran",stats["total_measurement"])
with c3: metric_card("Hari Ini",stats["today"])
st.info("Data riwayat dan distribusi status gizi akan tampil setelah pengukuran pertama disimpan.")
