from PyQt6.QtWidgets import QWidget, QLineEdit,QGridLayout, QPushButton, QVBoxLayout, QLabel, QCheckBox,QTableWidget, QHBoxLayout
from utils.theme_helper import apply_theme, style_button, style_table, style_label,tighten_layout,style_combo,style_input


from PyQt6.QtCore import Qt
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clinic Login")
        self.init_ui()
        apply_theme(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
    def init_ui(self):
        # Başlık etiketi
        self.label = QLabel("Login to System")
        style_label(self.label)

        # Kullanıcı adı
        self.username_input = QLineEdit()
        style_input(self.username_input)

        # Şifre
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        style_input(self.password_input)

        # Remember me
        self.remember_me = QCheckBox("Remember me")
        self.remember_me.setStyleSheet("font-size: 10pt; color: #333333;")

        # Butonlar
        self.login_button = QPushButton("Login")
        style_button(self.login_button)

        self.register_button = QPushButton("Register")
        style_button(self.register_button)

        self.forgot_button = QPushButton("Forgot Password")
        style_button(self.forgot_button)

        # GridLayout ile responsive form
        form_layout = QGridLayout()
        form_layout.setSpacing(12)

        form_layout.addWidget(QLabel("Username"), 0, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.username_input, 0, 1)

        form_layout.addWidget(QLabel("Password"), 1, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.password_input, 1, 1)

        form_layout.addWidget(self.remember_me, 2, 1)

        # Butonlar alt satırda yan yana
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.forgot_button)

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)