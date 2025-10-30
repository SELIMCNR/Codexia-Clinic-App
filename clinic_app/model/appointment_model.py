import sqlite3

class AppointmentModel:
    def __init__(self, db_path="clinic.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            doctor_name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_appointment(self, patient, doctor, date, time):
        if self.is_conflict(doctor, date, time):
            return False
        query = "INSERT INTO appointments (patient_name, doctor_name, date, time) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (patient, doctor, date, time))
        self.conn.commit()
        return True

    def is_conflict(self, doctor, date, time):
        query = "SELECT * FROM appointments WHERE doctor_name=? AND date=? AND time=?"
        cursor = self.conn.execute(query, (doctor, date, time))
        return cursor.fetchone() is not None

    def get_appointments(self):
        query = "SELECT * FROM appointments ORDER BY date, time"
        return self.conn.execute(query).fetchall()
    def delete_appointment(self, appointment_id):
        query = "DELETE FROM appointments WHERE id=?"
        self.conn.execute(query, (appointment_id,))
        self.conn.commit()