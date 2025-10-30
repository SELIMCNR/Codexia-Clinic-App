from PyQt6.QtWidgets import QMessageBox
from model.user_model import UserModel

class UserController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()
        self.connect_signals()
        self.load_users()

    def connect_signals(self):
        self.view.update_role_button.clicked.connect(self.handle_role_update)
        self.view.reset_password_button.clicked.connect(self.handle_password_reset)

    def load_users(self):
        users = self.model.get_all_users()
        self.view.table.setRowCount(len(users))
        for row, user in enumerate(users):
            for col, value in enumerate(user):
                self.view.table.setItem(row, col, self._item(str(value)))

    def handle_role_update(self):
        selected = self.view.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self.view, "Error", "Please select a user.")
            return

        user_id = int(self.view.table.item(selected, 0).text())
        new_role = self.view.role_combo.currentText()
        self.model.update_role(user_id, new_role)
        QMessageBox.information(self.view, "Updated", "User role updated.")
        self.load_users()

    def handle_password_reset(self):
        selected = self.view.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self.view, "Error", "Please select a user.")
            return

        new_password = self.view.password_input.text()
        if not new_password:
            QMessageBox.warning(self.view, "Error", "Please enter a new password.")
            return

        user_id = int(self.view.table.item(selected, 0).text())
        self.model.reset_password(user_id, new_password)
        QMessageBox.information(self.view, "Reset", "Password reset successfully.")
        self.view.password_input.clear()

    def _item(self, text):
        from PyQt6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)