from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
    QDateEdit, QPushButton, QTableWidget, QSplitter, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from utils.theme_helper import style_button, style_input, style_label, style_table, tighten_layout

class PatientWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Sol taraf (form alanı)
        form_layout = QVBoxLayout()
        tighten_layout(form_layout)

        form_layout.addWidget(QLabel("Name"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.name_input = QLineEdit()
        style_input(self.name_input)
        form_layout.addWidget(self.name_input)

        form_layout.addWidget(QLabel("Birth Date"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.birth_input = QDateEdit()
        self.birth_input.setCalendarPopup(True)
        self.birth_input.setFixedHeight(32)
        form_layout.addWidget(self.birth_input)

        form_layout.addWidget(QLabel("Phone"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.phone_input = QLineEdit()
        style_input(self.phone_input)
        form_layout.addWidget(self.phone_input)

        form_layout.addWidget(QLabel("Notes"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.notes_input = QTextEdit()
        self.notes_input.setFixedHeight(80)
        form_layout.addWidget(self.notes_input)

        self.add_button = QPushButton("Add Patient")
        style_button(self.add_button)
        form_layout.addWidget(self.add_button)

        form_widget = QWidget()
        form_widget.setLayout(form_layout)

        # Sağ taraf (tablo)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Birth Date", "Phone", "Notes"])
        style_table(self.table)

        # QSplitter ile bölme
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(form_widget)
        splitter.addWidget(self.table)
        splitter.setSizes([300, 700])  # başlangıçta sol 300px, sağ 700px

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(QLabel("Patient Management"))
        style_label(main_layout.itemAt(main_layout.count()-1).widget())
        main_layout.addWidget(splitter)

        self.setLayout(main_layout)