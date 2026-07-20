class DashboardService:
    def __init__(self,database): self.database=database
    def get_statistics(self):
        stats=self.database.get_statistics()
        stats.update(today=self.database.today_measurements(),percentage={},nutrition={})
        return stats
    def latest_measurements(self,limit=10): return []
    def risk_children(self): return []
