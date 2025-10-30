from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSplitter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from PyQt6.QtCore import Qt

from utils.theme_helper import (
    style_label, tighten_layout
)

class StatsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Sol taraf (istatistik özetleri)
        stats_layout = QVBoxLayout()
        tighten_layout(stats_layout)

        self.total_label = QLabel("Total Appointments: 0")
        style_label(self.total_label)
        stats_layout.addWidget(self.total_label)

        self.top_doctor_label = QLabel("Top Doctor: -")
        style_label(self.top_doctor_label)
        stats_layout.addWidget(self.top_doctor_label)

        stats_widget = QWidget()
        stats_widget.setLayout(stats_layout)

        # Sağ taraf (grafik alanı)
        self.figure = Figure(figsize=(6, 4))
        self.canvas = Canvas(self.figure)

        # QSplitter ile responsive görünüm
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(stats_widget)
        splitter.addWidget(self.canvas)
        splitter.setSizes([250, 750])

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)

        title_label = QLabel("Statistics Dashboard")
        style_label(title_label)
        main_layout.addWidget(title_label)
        main_layout.addWidget(splitter)

        self.setLayout(main_layout)

    def update_stats(self, total, top_doctor, distribution):
        # Etiketleri güncelle
        self.total_label.setText(f"Total Appointments: {total}")
        self.top_doctor_label.setText(f"Top Doctor: {top_doctor}")

        # Grafik güncelle
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        dates = list(distribution.keys())
        counts = list(distribution.values())
        ax.bar(dates, counts, color='#005fa1')
        ax.set_title("Daily Appointment Distribution", fontsize=12, fontweight="bold")
        ax.set_xlabel("Date")
        ax.set_ylabel("Appointments")
        ax.tick_params(axis='x', rotation=45)
        self.canvas.draw()