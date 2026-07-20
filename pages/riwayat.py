"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : riwayat.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from datetime import date
import pandas as pd
import streamlit as st

from services.service_container import services

st.title("Riwayat Pengukuran")

# =====================================================
# FILTER
# =====================================================

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    keyword = st.text_input(
        "Cari Nama atau NIK",
        placeholder="Masukkan nama atau NIK..."
    )

with col2:
    start_date = st.date_input(
        "Tanggal Awal",
        value=date.today().replace(day=1)
    )

with col3:
    end_date = st.date_input(
        "Tanggal Akhir",
        value=date.today()
    )

# =====================================================
# LOAD DATA
# =====================================================

if keyword:

    data = services.history.search(keyword)

else:

    data = services.history.filter_date(
        start_date,
        end_date
    )

# =====================================================
# TABLE
# =====================================================

if len(data) == 0:

    st.info("Belum ada data.")

else:

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )