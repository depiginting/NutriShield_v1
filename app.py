"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : app.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)

from utils.style import load_css
from utils.session import initialize_session

from components.layout.header import show_header
from components.layout.sidebar import show_sidebar
from components.layout.footer import show_footer


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)

# ==========================================================
# INITIALIZATION
# ==========================================================

initialize_session()

load_css()

# ==========================================================
# LAYOUT
# ==========================================================

show_sidebar()

show_header()

# ==========================================================
# HOME
# ==========================================================

st.markdown(
    """
    ## Selamat Datang 👋

    **NutriShield** adalah sistem pakar untuk penilaian status gizi anak
    berdasarkan Standar Pertumbuhan WHO.

    Silakan pilih menu di sidebar untuk memulai.
    """
)

st.info(
    "Gunakan menu **Pengukuran** untuk melakukan analisis status gizi anak."
)

# ==========================================================
# FOOTER
# ==========================================================

show_footer()