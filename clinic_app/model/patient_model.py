import sqlite3

class PatientModel:
    def __init__(self, db_path="clinic.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_date TEXT,
            phone TEXT,
            notes TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_patient(self, name, birth_date, phone, notes):
        query = "INSERT INTO patients (name, birth_date, phone, notes) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (name, birth_date, phone, notes))
        self.conn.commit()

    def get_all_patients(self):
        query = "SELECT * FROM patients ORDER BY name"
        return self.conn.execute(query).fetchall()