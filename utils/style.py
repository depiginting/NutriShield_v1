"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : style.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.theme import (
    PRIMARY_COLOR,
    BACKGROUND_COLOR,
    CARD_COLOR,
    TEXT_COLOR,
    TEXT_SECONDARY_COLOR,
    SUCCESS_COLOR,
    WARNING_COLOR,
    DANGER_COLOR,
    BORDER_COLOR,
    CARD_RADIUS,
    BUTTON_RADIUS,
    FONT_FAMILY,
)


def load_css():
    """Load custom CSS for NutriShield."""

    st.markdown(
        f"""
<style>

/* =====================================================
   GLOBAL
===================================================== */

html, body, [class*="css"] {{
    font-family: '{FONT_FAMILY}', sans-serif;
}}

.main {{
    background-color: {BACKGROUND_COLOR};
}}

/* =====================================================
   HEADER
===================================================== */

.app-title {{
    font-size:30px;
    font-weight:700;
    color:{PRIMARY_COLOR};
}}

.app-subtitle {{
    font-size:15px;
    color:{TEXT_SECONDARY_COLOR};
}}

/* =====================================================
   CARD
===================================================== */

.card {{
    background:{CARD_COLOR};
    padding:20px;
    border-radius:{CARD_RADIUS}px;
    border:1px solid {BORDER_COLOR};
    box-shadow:0 2px 8px rgba(0,0,0,.05);
    margin-bottom:15px;
}}

/* =====================================================
   METRIC
===================================================== */

.metric-title {{
    font-size:14px;
    color:{TEXT_SECONDARY_COLOR};
}}

.metric-value {{
    font-size:28px;
    font-weight:bold;
    color:{TEXT_COLOR};
}}

/* =====================================================
   STATUS
===================================================== */

.status-normal {{
    color:{SUCCESS_COLOR};
    font-weight:bold;
}}

.status-warning {{
    color:{WARNING_COLOR};
    font-weight:bold;
}}

.status-danger {{
    color:{DANGER_COLOR};
    font-weight:bold;
}}

/* =====================================================
   BUTTON
===================================================== */

.stButton > button {{
    width:100%;
    border-radius:{BUTTON_RADIUS}px;
    font-weight:600;
    height:42px;
}}

</style>
""",
        unsafe_allow_html=True,
    )