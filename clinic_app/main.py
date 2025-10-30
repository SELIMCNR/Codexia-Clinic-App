from PyQt6.QtWidgets import QApplication
from view.login_view import LoginWindow
from controller.login_controller import LoginController
from controller.register_controller import RegisterController
from view.register_view import RegisterWindow
from view.forgot_password_view import ForgotPasswordWindow
from controller.forgot_controller import ForgotPasswordController

# Global referanslar
windows = {}



controllers = {}  # Controller referanslarını burada tutacağız

def start_register():
        windows["register"] = RegisterWindow()
        controllers["register"] = RegisterController(windows["register"])  # Artık kaybolmaz
        windows["register"].show()

def start_login():
        windows["login"] = LoginWindow()
        controllers["login"] = LoginController(windows["login"])
        windows["login"].show()

def start_forgot():
        windows["forgot"] = ForgotPasswordWindow()
        controllers["forgot"] = ForgotPasswordController(windows["forgot"])
        windows["forgot"].show()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    start_login()

    # Buton bağlantıları login penceresi açıldıktan sonra yapılmalı
    windows["login"].register_button.clicked.connect(start_register)
    windows["login"].forgot_button.clicked.connect(start_forgot)

    sys.exit(app.exec())