"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : sidebar.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.settings import APP_NAME, APP_VERSION


def show_sidebar():
    """
    Display application sidebar.
    """

    with st.sidebar:

        st.title(APP_NAME)

        st.caption(f"Version {APP_VERSION}")

        st.divider()

        st.page_link("app.py", label="Dashboard")

        st.page_link(
            "pages/pengukuran.py",
            label="Pengukuran",
        )

        st.page_link(
            "pages/riwayat.py",
            label="Riwayat",
        )

        st.page_link(
            "pages/grafik_who.py",
            label="Grafik WHO",
        )

        st.page_link(
            "pages/laporan.py",
            label="Laporan",
        )

        st.page_link(
            "pages/pengaturan.py",
            label="Pengaturan",
        )

        st.page_link(
            "pages/tentang.py",
            label="Tentang",
        )

        st.divider()

        st.caption("© NutriShield")