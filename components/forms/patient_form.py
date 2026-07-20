"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : patient_form.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from datetime import date

import streamlit as st


def calculate_age_in_months(birth_date: date) -> int:
    """
    Calculate age in completed months.
    """

    today = date.today()

    months = (
        (today.year - birth_date.year) * 12
        + (today.month - birth_date.month)
    )

    if today.day < birth_date.day:
        months -= 1

    return max(months, 0)


def patient_form():
    """
    Display patient identity form.

    Returns
    -------
    dict
        Patient information.
    """

    st.subheader("Identitas Anak")

    nik = st.text_input(
        "NIK",
        placeholder="Masukkan Nomor Induk Kependudukan",
    )

    nama = st.text_input(
        "Nama Lengkap",
        placeholder="Masukkan nama anak",
    )

    gender = st.radio(
        "Jenis Kelamin",
        options=["L", "P"],
        horizontal=True,
    )

    tanggal_lahir = st.date_input(
        "Tanggal Lahir",
        value=date.today(),
        max_value=date.today(),
    )

    umur_bulan = calculate_age_in_months(tanggal_lahir)

    st.text_input(
        "Umur (Bulan)",
        value=str(umur_bulan),
        disabled=True,
    )

    return {
        "nik": nik.strip(),
        "nama": nama.strip(),
        "gender": gender,
        "tanggal_lahir": tanggal_lahir,
        "umur_bulan": umur_bulan,
    }