from PyQt6.QtWidgets import QMessageBox
from model.user_model import UserModel

class ForgotPasswordController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()
        self.connect_signals()

    def connect_signals(self):
        self.view.fetch_question_button.clicked.connect(self.fetch_question)
        self.view.reset_button.clicked.connect(self.handle_reset)

    def fetch_question(self):
        username = self.view.username_input.text()
        question = self.model.get_security_question(username)
        if question:
            self.view.security_question_label.setText(question)
        else:
            QMessageBox.warning(self.view, "Error", "Username not found.")

    def handle_reset(self):
        username = self.view.username_input.text()
        answer = self.view.security_answer_input.text()
        new_password = self.view.new_password_input.text()

        if self.model.verify_security_answer(username, answer):
            self.model.update_password(username, new_password)
            QMessageBox.information(self.view, "Success", "Password updated.")
            self.view.close()
        else:
            QMessageBox.warning(self.view, "Error", "Incorrect security answer.")