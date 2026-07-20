"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : history_service.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from datetime import date


class HistoryService:
    """
    Service for measurement history.
    """

    def __init__(self, database):
        self.database = database

    # =====================================================
    # HISTORY
    # =====================================================

    def get_all(self):
        """
        Get all measurement history.
        """
        return self.database.get_all_measurements()

    def get_by_patient(self, patient_id):
        """
        Get history by patient ID.
        """
        return self.database.get_history(patient_id)

    def search(self, keyword):
        """
        Search by NIK or patient name.
        """
        return self.database.search_measurements(keyword)

    def filter_date(self, start_date, end_date):
        """
        Filter history by date.
        """
        return self.database.filter_measurements(
            start_date=start_date,
            end_date=end_date,
        )

    def delete(self, measurement_id):
        """
        Delete measurement.
        """
        return self.database.delete_measurement(
            measurement_id
        )

    def statistics(self):
        """
        Get simple statistics.
        """

        history = self.database.get_all_measurements()

        return {
            "total_measurement": len(history),
            "today": sum(
                1
                for row in history
                if row["tanggal"] == str(date.today())
            ),
        }