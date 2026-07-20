"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : status_badge.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.theme import STATUS_COLOR


def status_badge(status: str):
    """
    Display nutrition status badge.
    """

    color = STATUS_COLOR.get(status, "#1565C0")

    st.markdown(
        f"""
        <span style="
            background:{color};
            color:white;
            padding:6px 12px;
            border-radius:20px;
            font-size:13px;
            font-weight:600;
        ">
            {status}
        </span>
        """,
        unsafe_allow_html=True,
    )