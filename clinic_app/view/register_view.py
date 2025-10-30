from PyQt6.QtWidgets import QWidget, QLineEdit,QGridLayout, QPushButton, QVBoxLayout, QLabel, QComboBox,QTableWidget
from utils.theme_helper import apply_theme, style_button, style_table, style_label,tighten_layout,style_combo,style_input


from PyQt6.QtCore import Qt
class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register New User")
        self.init_ui()
        apply_theme(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setMinimumSize(1024, 768)
    def init_ui(self):
        # Başlık etiketi
        self.label = QLabel("User Registration")
        style_label(self.label)

        # Alanlar
        self.username_input = QLineEdit()
        style_input(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        style_input(self.password_input)

        self.role_combo = QComboBox()
        self.role_combo.addItems(["Doctor", "Secretary", "Admin"])
        style_combo(self.role_combo)

        self.security_question_input = QLineEdit()
        style_input(self.security_question_input)

        self.security_answer_input = QLineEdit()
        style_input(self.security_answer_input)

        self.register_button = QPushButton("Register")
        style_button(self.register_button)

        # GridLayout ile responsive form
        form_layout = QGridLayout()
        form_layout.setSpacing(12)

        form_layout.addWidget(QLabel("Username"), 0, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.username_input, 0, 1)

        form_layout.addWidget(QLabel("Password"), 1, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.password_input, 1, 1)

        form_layout.addWidget(QLabel("Role"), 2, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.role_combo, 2, 1)

        form_layout.addWidget(QLabel("Security Question"), 3, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.security_question_input, 3, 1)

        form_layout.addWidget(QLabel("Security Answer"), 4, 0)
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        form_layout.addWidget(self.security_answer_input, 4, 1)

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.register_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)