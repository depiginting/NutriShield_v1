"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : session.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st


DEFAULT_SESSION = {
    "patient": {},
    "measurement": {},
    "result": None,
}


def initialize_session():
    """
    Initialize application session.
    """

    if "measurement" not in st.session_state:
        st.session_state.measurement = DEFAULT_SESSION.copy()


def get_measurement():
    """
    Get current measurement session.
    """

    return st.session_state.measurement


def save_measurement(patient, measurement, result):
    """
    Save measurement data to session.
    """

    st.session_state.measurement = {
        "patient": patient,
        "measurement": measurement,
        "result": result,
    }


def clear_measurement():
    """
    Clear measurement session.
    """

    st.session_state.measurement = DEFAULT_SESSION.copy()


def has_result():
    """
    Check whether calculation result exists.
    """

    return st.session_state.measurement["result"] is not None


def get_result():
    """
    Get latest calculation result.
    """

    return st.session_state.measurement["result"]