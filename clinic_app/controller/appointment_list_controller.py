from PyQt6.QtWidgets import QMessageBox
from model.appointment_model import AppointmentModel

class AppointmentListController:
    def __init__(self, view):
        self.view = view
        self.model = AppointmentModel()
        self.connect_signals()
        self.load_appointments()

    def connect_signals(self):
        self.view.delete_button.clicked.connect(self.handle_delete)

    def load_appointments(self):
        appointments = self.model.get_appointments()
        self.view.table.setRowCount(len(appointments))
        for row, appt in enumerate(appointments):
            for col, value in enumerate(appt):  # ID dahil
                self.view.table.setItem(row, col, self._item(str(value)))

    def handle_delete(self):
        selected = self.view.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self.view, "Error", "Please select an appointment to delete.")
            return

        appt_id = self.view.table.item(selected, 0).text()
        self.model.delete_appointment(int(appt_id))
        QMessageBox.information(self.view, "Deleted", "Appointment deleted successfully.")
        self.load_appointments()

    def _item(self, text):
        from PyQt6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)