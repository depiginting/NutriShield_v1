"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : service_container.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from core.anthropometry import Anthropometry
from core.database import Database

from services.measurement_service import MeasurementService
from services.graph_service import GraphService
from services.dashboard_service import DashboardService

class ServiceContainer:
    """
    Dependency Injection Container.

    Menyediakan instance database, engine,
    dan seluruh service yang digunakan aplikasi.
    """

    def __init__(self):

        # Shared Resources
        self.database = Database()
        self.engine = Anthropometry()

        # Services
        self.measurement = MeasurementService(
            database=self.database,
            engine=self.engine,
        )
        self.dashboard = DashboardService(
            database=self.database,
        )

        self.graph = GraphService(
            database=self.database,
        )

    def close(self):
        """
        Close shared resources.
        """
        self.database.close()


# Singleton Container
services = ServiceContainer()

