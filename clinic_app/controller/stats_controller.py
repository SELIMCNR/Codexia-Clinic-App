from model.stats_model import StatsModel

class StatsController:
    def __init__(self, view):
        self.view = view
        self.model = StatsModel()
        self.load_stats()

    def load_stats(self):
        total = self.model.get_total_appointments()
        top_doctor, count = self.model.get_top_doctor()
        distribution = self.model.get_daily_distribution()
        self.view.update_stats(total, f"{top_doctor} ({count})", distribution)