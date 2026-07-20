"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : dashboard_service.py
=========================================================
"""

from collections import Counter


class DashboardService:

    def __init__(self, database):
        self.database = database

    def get_statistics(self):
        """
        Return dashboard statistics.
        """

        stats = self.database.get_statistics()

        measurements = self.database.get_all_measurements()

        nutrition = Counter(
            row["nutrition_status"]
            for row in measurements
        )

        stats["nutrition"] = dict(nutrition)

        return stats

    def latest_measurements(self, limit=10):
        """
        Latest measurements.
        """

        history = self.database.get_all_measurements()

        return history[:limit]
    
    def get_statistics(self):

        stats = self.database.get_statistics()

        stats["today"] = self.database.today_measurements()

        stats["percentage"] = self.database.nutrition_percentage()

        stats["nutrition"] = self.database.nutrition_distribution()

        return stats
    
    def risk_children(self):

        return self.database.risk_children()