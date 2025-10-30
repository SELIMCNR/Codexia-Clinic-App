import json
import os
from PyQt6.QtWidgets import QMessageBox
from model.user_model import UserModel
from view.dashboard_view import DashboardWindow  # varsayım: bu modül var

REMEMBER_FILE = "remember_me.json"

class LoginController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()
        self.connect_signals()
        self.auto_login_if_remembered()
        self.failed_attempts = 0  # __init__ içinde tanımla

    def connect_signals(self):
        self.view.login_button.clicked.connect(self.handle_login)

    def auto_login_if_remembered(self):
        if os.path.exists(REMEMBER_FILE):
            with open(REMEMBER_FILE, "r") as f:
                data = json.load(f)
                username = data.get("username")
                password = data.get("password")
                role = self.model.verify_user(username, password)
                if role:
                    self.open_dashboard(role)

   
    def handle_login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        role = self.model.verify_user(username, password)

        if role:
            self.failed_attempts = 0
            QMessageBox.information(self.view, "Login Successful", f"Welcome, {role}")
            self.open_dashboard(role)
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 5:
                QMessageBox.critical(self.view, "Blocked", "Too many failed attempts. Please try again later.")
                self.view.login_button.setEnabled(False)
            else:
                QMessageBox.warning(self.view, "Login Failed", f"Invalid credentials. Attempt {self.failed_attempts}/5")

    def open_dashboard(self, role):
        self.view.close()
        self.dashboard = DashboardWindow(role=role)
        self.dashboard.show()
    