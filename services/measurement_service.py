"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : measurement_service.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from core.anthropometry import Anthropometry
from core.database import Database


class MeasurementService:

    def __init__(
        self,
        database,
        engine,
    ):

        self.database = database
        self.engine = engine

    # =====================================================
    # PATIENT
    # =====================================================

    def get_patient(self, nik):
        """
        Get patient by NIK.
        """
        return self.database.get_patient(nik)

    def create_patient(
        self,
        nik,
        nama,
        gender,
        tanggal_lahir,
    ):
        """
        Create new patient.
        """
        return self.database.add_patient(
            nik=nik,
            nama=nama,
            gender=gender,
            tanggal_lahir=tanggal_lahir,
        )

    # =====================================================
    # CALCULATION
    # =====================================================

    def calculate(
        self,
        gender,
        age_month,
        weight,
        height,
    ):
        """
        Calculate anthropometry.
        """

        return self.engine.calculate(
            gender=gender,
            age_month=age_month,
            weight=weight,
            height=height,
        )

    # =====================================================
    # SAVE RESULT
    # =====================================================

    def save_measurement(
        self,
        patient_id,
        result,
        tanggal,
    ):
        """
        Save measurement result.
        """

        return self.database.save_measurement(
            patient_id=patient_id,
            result=result,
            tanggal=tanggal,
        )

    # =====================================================
    # HISTORY
    # =====================================================

    def get_history(self, patient_id):
        """
        Get patient measurement history.
        """

        return self.database.get_history(patient_id)

    # =====================================================
    # CLOSE
    # =====================================================

    def close(self):
        """
        Close database connection.
        """

        self.database.close()