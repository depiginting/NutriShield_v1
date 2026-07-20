"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : metric_card.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from config.theme import (
    CARD_COLOR,
    PRIMARY_COLOR,
    TEXT_COLOR,
    TEXT_SECONDARY_COLOR,
    CARD_RADIUS,
)


def metric_card(
    title: str,
    value,
    icon: str = "",
    color: str = PRIMARY_COLOR,
):
    """
    Display metric card.

    Parameters
    ----------
    title : str
        Card title.

    value : any
        Metric value.

    icon : str
        Material icon.

    color : str
        Card accent color.
    """

    st.markdown(
        f"""
        <div style="
            background:{CARD_COLOR};
            border-radius:{CARD_RADIUS}px;
            padding:18px;
            border-left:6px solid {color};
            box-shadow:0 2px 6px rgba(0,0,0,.08);
            margin-bottom:12px;
        ">

            <div style="
                font-size:14px;
                color:{TEXT_SECONDARY_COLOR};
                margin-bottom:8px;
            ">
                {icon} {title}
            </div>

            <div style="
                font-size:34px;
                font-weight:700;
                color:{TEXT_COLOR};
            ">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )