"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : measurement_form.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from datetime import date

import streamlit as st


def measurement_form():
    """
    Display anthropometric measurement form.

    Returns
    -------
    dict
        Measurement data and button states.
    """

    st.subheader("Data Pengukuran")

    weight = st.number_input(
        "Berat Badan (kg)",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=0.1,
        format="%.1f",
    )

    height = st.number_input(
        "Tinggi / Panjang Badan (cm)",
        min_value=30.0,
        max_value=150.0,
        value=30.0,
        step=0.1,
        format="%.1f",
    )

    tanggal = st.date_input(
        "Tanggal Pengukuran",
        value=date.today(),
        max_value=date.today(),
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        calculate = st.button(
            "Hitung",
            type="primary",
            use_container_width=True,
        )

    with col2:
        save = st.button(
            "Simpan",
            use_container_width=True,
        )

    with col3:
        reset = st.button(
            "Reset",
            use_container_width=True,
        )

    return {
        "weight": weight,
        "height": height,
        "tanggal": tanggal,
        "calculate": calculate,
        "save": save,
        "reset": reset,
    }