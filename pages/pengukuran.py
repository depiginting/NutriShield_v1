"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : pengukuran.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

import streamlit as st

from core.anthropometry import Anthropometry
from core.database import Database
from services.measurement_service import MeasurementService

from components.forms.patient_form import patient_form
from components.forms.measurement_form import measurement_form
from components.panels.result_panel import result_panel


# =====================================================
# INITIALIZATION
# =====================================================

if "measurement_result" not in st.session_state:
    st.session_state.measurement_result = None

db = Database()
engine = Anthropometry()

service = MeasurementService(
    database=db,
    engine=engine,
)


# =====================================================
# PAGE
# =====================================================

st.title("Pengukuran Status Gizi")

col1, col2, col3 = st.columns([1.2, 1, 1.2])

# =====================================================
# IDENTITAS
# =====================================================

with col1:
    patient = patient_form()

# =====================================================
# PENGUKURAN
# =====================================================

with col2:
    measurement = measurement_form()

# =====================================================
# HITUNG
# =====================================================

if measurement["calculate"]:

    result = service.calculate(
        gender=patient["gender"],
        age_month=patient["umur_bulan"],
        weight=measurement["weight"],
        height=measurement["height"],
    )

    st.session_state.measurement_result = result

# =====================================================
# HASIL
# =====================================================

with col3:

    result_panel(
        st.session_state.measurement_result
    )

# =====================================================
# SIMPAN
# =====================================================

if measurement["save"]:

    patient_db = service.get_patient(
        patient["nik"]
    )

    if patient_db is None:

        patient_id = service.create_patient(
            nik=patient["nik"],
            nama=patient["nama"],
            gender=patient["gender"],
            tanggal_lahir=patient["tanggal_lahir"],
        )

    else:

        patient_id = patient_db["id"]

    service.save_measurement(
        patient_id=patient_id,
        result=st.session_state.measurement_result,
        tanggal=measurement["tanggal"],
    )

    st.success("Data berhasil disimpan.")

# =====================================================
# RESET
# =====================================================

if measurement["reset"]:

    st.session_state.measurement_result = None

    st.rerun()

# =====================================================
# CLOSE
# =====================================================

service.close()