from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel,QTableWidget
from utils.theme_helper import apply_theme, style_button, style_table, style_label,style_input,style_combo,tighten_layout


from PyQt6.QtCore import Qt
class ForgotPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Forgot Password")
        self.init_ui()
        apply_theme(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setMinimumSize(1024, 768)
    def init_ui(self):
        # Başlık etiketi
        self.label = QLabel("Reset Password")
        style_label(self.label)

        # Kullanıcı adı girişi
        self.username_input = QLineEdit()
        style_input(self.username_input)

        # Güvenlik sorusu etiketi
        self.security_question_label = QLabel("Security Question will appear here")
        style_label(self.security_question_label)

        # Güvenlik cevabı girişi
        self.security_answer_input = QLineEdit()
        style_input(self.security_answer_input)

        # Yeni şifre girişi
        self.new_password_input = QLineEdit()
        self.new_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        style_input(self.new_password_input)

        # Butonlar
        self.fetch_question_button = QPushButton("Get Security Question")
        style_button(self.fetch_question_button)

        self.reset_button = QPushButton("Reset Password")
        style_button(self.reset_button)

        # Layout
        layout = QVBoxLayout()
        tighten_layout(layout)  # boşlukları profesyonel hale getirir

        layout.addWidget(self.label)

        layout.addWidget(QLabel("Username"))
        style_label(layout.itemAt(layout.count()-1).widget())
        layout.addWidget(self.username_input)
        layout.addWidget(self.fetch_question_button)

        layout.addWidget(self.security_question_label)

        layout.addWidget(QLabel("Security Answer"))
        style_label(layout.itemAt(layout.count()-1).widget())
        layout.addWidget(self.security_answer_input)

        layout.addWidget(QLabel("New Password"))
        style_label(layout.itemAt(layout.count()-1).widget())
        layout.addWidget(self.new_password_input)

        layout.addWidget(self.reset_button)

        self.setLayout(layout)