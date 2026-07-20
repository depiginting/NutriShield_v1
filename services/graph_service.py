"""
=========================================================
NutriShield

Graph Service

=========================================================
"""

class GraphService:

    def __init__(
        self,
        database,
    ):

        self.database = database

    def patient_growth(
        self,
        patient_id,
    ):
        """
        Return growth history.
        """

        history = self.database.get_history(
            patient_id
        )

        return history