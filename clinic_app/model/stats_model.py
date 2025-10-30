import sqlite3
from collections import Counter

class StatsModel:
    def __init__(self, db_path="clinic.db"):
        self.conn = sqlite3.connect(db_path)

    def get_total_appointments(self):
        query = "SELECT COUNT(*) FROM appointments"
        return self.conn.execute(query).fetchone()[0]

    def get_top_doctor(self):
        query = "SELECT doctor_name FROM appointments"
        doctors = [row[0] for row in self.conn.execute(query).fetchall()]
        return Counter(doctors).most_common(1)[0] if doctors else ("None", 0)

    def get_daily_distribution(self):
        query = "SELECT date FROM appointments"
        dates = [row[0] for row in self.conn.execute(query).fetchall()]
        return Counter(dates)