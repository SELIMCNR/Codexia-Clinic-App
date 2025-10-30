from PyQt6.QtWidgets import QMessageBox
from model.user_model import UserModel

class RegisterController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()
        self.connect_signals()

    def connect_signals(self):
        self.view.register_button.clicked.connect(self.handle_register)

    def handle_register(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        role = self.view.role_combo.currentText()
        question = self.view.security_question_input.text()
        answer = self.view.security_answer_input.text()

        if not username or not password or not question or not answer:
            QMessageBox.warning(self.view, "Error", "All fields are required.")
            return

        if not self.model.is_valid_password(password):
            QMessageBox.warning(self.view, "Error", "Password must be at least 6 characters and include letters and numbers.")
            return

        success = self.model.add_user(username, password, role, question, answer)
        if success:
            QMessageBox.information(self.view, "Success", "User registered successfully.")
            self.view.close()
        else:
            QMessageBox.warning(self.view, "Error", "Username already exists.")