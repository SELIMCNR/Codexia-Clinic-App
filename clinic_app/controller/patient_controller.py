from PyQt6.QtWidgets import QMessageBox
from model.patient_model import PatientModel

class PatientController:
    def __init__(self, view):
        self.view = view
        self.model = PatientModel()
        self.connect_signals()
        self.load_patients()

    def connect_signals(self):
        self.view.add_button.clicked.connect(self.handle_add)

    def handle_add(self):
        name = self.view.name_input.text()
        birth_date = self.view.birth_input.date().toString("yyyy-MM-dd")
        phone = self.view.phone_input.text()
        notes = self.view.notes_input.toPlainText()

        if not name:
            QMessageBox.warning(self.view, "Error", "Patient name is required.")
            return

        self.model.add_patient(name, birth_date, phone, notes)
        QMessageBox.information(self.view, "Success", "Patient added successfully.")
        self.view.name_input.clear()
        self.view.phone_input.clear()
        self.view.notes_input.clear()
        self.load_patients()

    def load_patients(self):
        patients = self.model.get_all_patients()
        self.view.table.setRowCount(len(patients))
        for row, patient in enumerate(patients):
            for col, value in enumerate(patient[1:]):  # Skip ID
                self.view.table.setItem(row, col, self._item(str(value)))

    def _item(self, text):
        from PyQt6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)