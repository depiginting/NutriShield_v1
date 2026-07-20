"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : footer.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.settings import (
    APP_NAME,
    APP_VERSION,
    AUTHOR,
)


def show_footer():
    """
    Display application footer.
    """

    st.divider()

    st.caption(
        f"{APP_NAME} v{APP_VERSION} | Developed by {AUTHOR}"
    )