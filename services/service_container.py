from core.anthropometry import Anthropometry
from core.database import Database
from services.dashboard_service import DashboardService
from services.graph_service import GraphService
from services.history_service import HistoryService
from services.measurement_service import MeasurementService

class ServiceContainer:
    def __init__(self):
        self.database=Database(); self.engine=Anthropometry()
        self.measurement=MeasurementService(self.database,self.engine)
        self.dashboard=DashboardService(self.database)
        self.graph=GraphService(self.database)
        self.history=HistoryService(self.database)
    def close(self): self.database.close()
services=ServiceContainer()
