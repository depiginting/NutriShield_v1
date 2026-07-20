"""
====================================================
NutriShield
Input Validator
Author : Depi Ginting
====================================================
"""

from core.config import (
    GENDER,
    INDICATORS,
    MIN_AGE_MONTH,
    MAX_AGE_MONTH
)


class Validator:

    @staticmethod
    def gender(gender: str):

        if gender is None:
            raise ValueError("Jenis kelamin tidak boleh kosong.")

        gender = gender.upper()

        if gender not in GENDER:
            raise ValueError(
                "Jenis kelamin harus L atau P."
            )

        return GENDER[gender]

    # ======================================================

    @staticmethod
    def indicator(indicator: str):

        indicator = indicator.lower()

        if indicator not in INDICATORS:
            raise ValueError(
                f"Indikator '{indicator}' tidak tersedia."
            )

        return indicator

    # ======================================================

    @staticmethod
    def age(age_month: float):

        if age_month is None:
            raise ValueError("Umur tidak boleh kosong.")

        age_month = float(age_month)

        if age_month < MIN_AGE_MONTH:
            raise ValueError("Umur tidak boleh kurang dari 0 bulan.")

        if age_month > MAX_AGE_MONTH:
            raise ValueError(
                f"Umur maksimum {MAX_AGE_MONTH} bulan."
            )

        return age_month

    # ======================================================

    @staticmethod
    def weight(weight: float):

        if weight is None:
            raise ValueError("Berat badan tidak boleh kosong.")

        weight = float(weight)

        if weight <= 0:
            raise ValueError(
                "Berat badan harus lebih dari 0 kg."
            )

        if weight > 200:
            raise ValueError(
                "Berat badan tidak masuk akal."
            )

        return weight

    # ======================================================

    @staticmethod
    def height(height: float):

        if height is None:
            raise ValueError(
                "Tinggi/Panjang badan tidak boleh kosong."
            )

        height = float(height)

        if height <= 0:
            raise ValueError(
                "Tinggi/Panjang badan harus lebih dari 0 cm."
            )

        if height > 250:
            raise ValueError(
                "Tinggi/Panjang badan tidak masuk akal."
            )

        return height

    # ======================================================

    @staticmethod
    def measurement(gender,
                    age_month,
                    weight,
                    height):

        return {

            "gender": Validator.gender(gender),

            "age_month": Validator.age(age_month),

            "weight": Validator.weight(weight),

            "height": Validator.height(height)

        }