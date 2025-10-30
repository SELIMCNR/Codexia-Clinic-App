from PyQt6.QtWidgets import QWidget,QSplitter, QVBoxLayout, QLabel, QTableWidget,QDateEdit,QComboBox, QTableWidgetItem, QPushButton
from utils.theme_helper import apply_theme, style_button, style_table, style_label,tighten_layout,style_combo


from PyQt6.QtCore import Qt
class AppointmentListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appointment List")
        self.init_ui()
        apply_theme(self)
 
        
    def init_ui(self):
        # Sol taraf (tablo)
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Patient", "Doctor", "Date", "Time"])
        self.table.setSelectionBehavior(self.table.SelectionBehavior.SelectRows)
        style_table(self.table)

        self.delete_button = QPushButton("Delete Selected Appointment")
        style_button(self.delete_button)

        table_layout = QVBoxLayout()
        tighten_layout(table_layout)
        table_layout.addWidget(QLabel("All Appointments"))
        style_label(table_layout.itemAt(table_layout.count()-1).widget())
        table_layout.addWidget(self.table)
        table_layout.addWidget(self.delete_button)

        table_widget = QWidget()
        table_widget.setLayout(table_layout)

        # Sağ taraf (filtre paneli)
        filter_layout = QVBoxLayout()
        tighten_layout(filter_layout)

        filter_layout.addWidget(QLabel("Filter by Doctor"))
        style_label(filter_layout.itemAt(filter_layout.count()-1).widget())
        self.doctor_filter = QComboBox()
        self.doctor_filter.addItems(["All", "Dr. A", "Dr. B", "Dr. C"])
        style_combo(self.doctor_filter)
        filter_layout.addWidget(self.doctor_filter)

        filter_layout.addWidget(QLabel("Filter by Date"))
        style_label(filter_layout.itemAt(filter_layout.count()-1).widget())
        self.date_filter = QDateEdit()
        self.date_filter.setCalendarPopup(True)
        self.date_filter.setFixedHeight(32)
        filter_layout.addWidget(self.date_filter)

        self.apply_filter_button = QPushButton("Apply Filter")
        style_button(self.apply_filter_button)
        filter_layout.addWidget(self.apply_filter_button)

        filter_widget = QWidget()
        filter_widget.setLayout(filter_layout)

        # QSplitter ile responsive görünüm
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(table_widget)
        splitter.addWidget(filter_widget)
        splitter.setSizes([700, 300])  # başlangıçta tablo geniş, filtre dar

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(splitter)

        self.setLayout(main_layout)