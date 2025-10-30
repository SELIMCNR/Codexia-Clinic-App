from PyQt6.QtWidgets import QMessageBox
from model.appointment_model import AppointmentModel

class AppointmentController:
    def __init__(self, view):
        self.view = view
        self.model = AppointmentModel()
        self.connect_signals()

    def connect_signals(self):
        self.view.create_button.clicked.connect(self.handle_create)

    def handle_create(self):
        patient = self.view.patient_input.text()
        doctor = self.view.doctor_combo.currentText()
        date = self.view.date_picker.date().toString("yyyy-MM-dd")
        time = self.view.time_picker.time().toString("HH:mm")

        if not patient:
            QMessageBox.warning(self.view, "Error", "Patient name is required.")
            return

        success = self.model.add_appointment(patient, doctor, date, time)
        if success:
            QMessageBox.information(self.view, "Success", "Appointment created successfully.")
            self.view.patient_input.clear()
        else:
            QMessageBox.warning(self.view, "Conflict", "This time slot is already booked for the selected doctor.")