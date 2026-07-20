"""
=========================================================
NutriShield

File : result_panel.py
=========================================================
"""

import streamlit as st


def result_panel(result: dict | None):
    """
    Display anthropometric analysis results.
    """

    st.subheader("Hasil Analisis")

    if result is None:
        st.info("Silakan lakukan pengukuran terlebih dahulu.")
        return

    st.metric(
        "BB/U",
        result["weight_for_age"]["status"],
        f'Z = {result["weight_for_age"]["zscore"]:.2f}',
    )

    st.metric(
        "TB/U",
        result["height_for_age"]["status"],
        f'Z = {result["height_for_age"]["zscore"]:.2f}',
    )

    st.metric(
        "BB/TB",
        result["weight_for_height"]["status"],
        f'Z = {result["weight_for_height"]["zscore"]:.2f}',
    )

    st.metric(
        "IMT/U",
        result["bmi_for_age"]["status"],
        f'Z = {result["bmi_for_age"]["zscore"]:.2f}',
    )

    st.success(
        f"Status Gizi : **{result['summary']['nutrition_status']}**"
    )

    st.info(result["summary"]["recommendation"])