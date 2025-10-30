from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication

# View ve Controller importları
from view.appointment_view import AppointmentWindow
from controller.appointment_controller import AppointmentController

from view.patient_view import PatientWindow
from controller.patient_controller import PatientController

from view.appointment_list_view import AppointmentListWindow
from controller.appointment_list_controller import AppointmentListController

from view.stats_view import StatsWindow
from controller.stats_controller import StatsController

from view.user_view import UserWindow
from controller.user_controller import UserController

from utils.theme_helper import (
    style_button, style_label, tighten_layout
)


class DashboardWindow(QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.init_ui()

    def init_ui(self):
        # Sol menü layout
        menu_layout = QVBoxLayout()
        tighten_layout(menu_layout)

        self.welcome_label = QLabel(f"Welcome, {self.role}")
        style_label(self.welcome_label)
        menu_layout.addWidget(self.welcome_label)

        # Menü butonları
        self.view_appointments_button = QPushButton("View Appointments")
        style_button(self.view_appointments_button)
        menu_layout.addWidget(self.view_appointments_button)

        self.stats_button = QPushButton("View Statistics")
        style_button(self.stats_button)
        menu_layout.addWidget(self.stats_button)

        if self.role in ["Doctor", "Secretary"]:
            self.appointment_button = QPushButton("Manage Appointments")
            style_button(self.appointment_button)
            menu_layout.addWidget(self.appointment_button)

            self.patient_button = QPushButton("Manage Patients")
            style_button(self.patient_button)
            menu_layout.addWidget(self.patient_button)

        if self.role == "Admin":
            self.user_button = QPushButton("User Management")
            style_button(self.user_button)
            menu_layout.addWidget(self.user_button)

        menu_layout.addStretch()

        # Menü widget + ScrollArea
        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(menu_widget)
        scroll_area.setStyleSheet("border: none;")

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(scroll_area)

        central = QWidget()
        central.setLayout(main_layout)
        self.setCentralWidget(central)

        # 🔗 Buton bağlantıları → ayrı pencere aç
        self.view_appointments_button.clicked.connect(self.open_appointment_list)
        self.stats_button.clicked.connect(self.open_stats)

        if self.role in ["Doctor", "Secretary"]:
            self.appointment_button.clicked.connect(self.open_appointment)
            self.patient_button.clicked.connect(self.open_patient)

        if self.role == "Admin":
            self.user_button.clicked.connect(self.open_user)

        # ✅ Responsive: pencereyi ekran çözünürlüğüne göre aç
        screen = QGuiApplication.primaryScreen()
        size = screen.availableGeometry()
        self.resize(int(size.width() * 0.5), int(size.height() * 0.7))
        self.showMaximized()

    # Ayrı pencere açan fonksiyonlar
    def open_appointment_list(self):
        self.appointment_window = AppointmentListWindow()
        self.appointment_controller = AppointmentListController(self.appointment_window)
        self.appointment_window.show()

    def open_stats(self):
        self.stats_window = StatsWindow()
        self.stats_controller = StatsController(self.stats_window)
        self.stats_window.show()

    def open_appointment(self):
        self.appointment_window = AppointmentWindow()
        self.appointment_controller = AppointmentController(self.appointment_window)
        self.appointment_window.show()

    def open_patient(self):
        self.patient_window = PatientWindow()
        self.patient_controller = PatientController(self.patient_window)
        self.patient_window.show()

    def open_user(self):
        self.user_window = UserWindow()
        self.user_controller = UserController(self.user_window)
        self.user_window.show()