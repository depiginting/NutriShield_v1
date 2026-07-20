"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : header.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.settings import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    LOGO_PATH,
)


def show_header():
    """
    Display application header.
    """

    col_logo, col_title = st.columns([1, 8])

    with col_logo:
        try:
            st.image(LOGO_PATH, width=70)
        except Exception:
            st.empty()

    with col_title:
        st.markdown(
            f"""
            <div class="app-title">{APP_NAME}</div>
            <div class="app-subtitle">
                {APP_DESCRIPTION}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.caption(f"Version {APP_VERSION}")

    st.divider()