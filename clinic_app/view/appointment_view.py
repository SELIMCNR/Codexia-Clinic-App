from PyQt6.QtWidgets import QWidget,QSplitter,QTableWidget,QLineEdit, QComboBox, QDateEdit, QTimeEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import QDate, QTime
from utils.theme_helper import apply_theme, style_button, style_table, style_label,tighten_layout,style_combo,style_input


from PyQt6.QtCore import Qt
class AppointmentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Appointment")
        self.init_ui()
        apply_theme(self)
        
    def init_ui(self):
        # Sol taraf (form)
        form_layout = QVBoxLayout()
        tighten_layout(form_layout)

        form_layout.addWidget(QLabel("Patient Name"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.patient_input = QLineEdit()
        style_input(self.patient_input)
        form_layout.addWidget(self.patient_input)

        form_layout.addWidget(QLabel("Doctor"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.doctor_combo = QComboBox()
        style_combo(self.doctor_combo)
        form_layout.addWidget(self.doctor_combo)

        form_layout.addWidget(QLabel("Date"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setFixedHeight(32)
        form_layout.addWidget(self.date_picker)

        form_layout.addWidget(QLabel("Time"))
        style_label(form_layout.itemAt(form_layout.count()-1).widget())
        self.time_picker = QTimeEdit()
        self.time_picker.setFixedHeight(32)
        form_layout.addWidget(self.time_picker)

        self.create_button = QPushButton("Create Appointment")
        style_button(self.create_button)
        form_layout.addWidget(self.create_button)

        form_widget = QWidget()
        form_widget.setLayout(form_layout)

        # Sağ taraf (tablo)
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Patient", "Doctor", "Date", "Time"])
        style_table(self.table)

        # QSplitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(form_widget)
        splitter.addWidget(self.table)
        splitter.setSizes([350, 650])

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(QLabel("Appointment Management"))
        style_label(main_layout.itemAt(main_layout.count()-1).widget())
        main_layout.addWidget(splitter)

        self.setLayout(main_layout)