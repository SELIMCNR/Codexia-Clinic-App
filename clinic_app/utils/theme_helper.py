from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QTableWidget, QLabel, QLineEdit, QComboBox, QLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette, QGuiApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt

def apply_theme(widget: QWidget):
    # Genel font
    font = QFont("Segoe UI", 10)
    widget.setFont(font)

    # Renk paleti
    palette = widget.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#f0f2f5"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#005fa1"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#333333"))
    widget.setPalette(palette)

    # Minimum boyut
    widget.setMinimumSize(800, 600)

    # ✅ Responsive ekran boyutlandırma
    screen = QGuiApplication.primaryScreen()
    size = screen.availableGeometry()
    widget.resize(int(size.width() * 0.9), int(size.height() * 0.9))
    widget.showMaximized()

def tighten_layout(layout: QLayout):
    layout.setContentsMargins(20, 20, 20, 20)  # Kenar boşlukları
    layout.setSpacing(10)  # Bileşenler arası boşluk
# Modern buton stili (Apple + Microsoft Fluent)
def style_button(button: QPushButton):
    button.setFixedHeight(36)
    button.setStyleSheet("""
        QPushButton {
            background-color: #007aff;   /* Apple mavi */
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: 500;
            font-family: 'Helvetica Neue', 'Segoe UI';
        }
        QPushButton:hover {
            background-color: #0060df;   /* Hover için daha koyu mavi */
        }
        QPushButton:pressed {
            background-color: #004bb5;   /* Basılıyken daha koyu */
        }
        QPushButton:disabled {
            background-color: #d1d1d6;   /* Apple gri */
            color: #8e8e93;
        }
    """)


# Tablo stili (Apple flat + Fluent header)
def style_table(table: QTableWidget):
    table.setAlternatingRowColors(True)
    table.setMinimumHeight(300)
    table.setStyleSheet("""
        QTableWidget {
            background-color: #ffffff;
            alternate-background-color: #f5f5f7;  /* Apple açık gri */
            gridline-color: #d1d1d6;
            font-size: 10pt;
            font-family: 'Helvetica Neue', 'Segoe UI';
        }
        QHeaderView::section {
            background-color: #007aff;   /* Apple mavi */
            color: white;
            font-weight: 600;
            padding: 6px;
            border: none;
        }
    """)


# Label stili (Apple sade tipografi)
def style_label(label: QLabel):
    label.setStyleSheet("""
        QLabel {
            font-size: 11pt;
            font-weight: 500;
            color: #1d1d1f;   /* Apple koyu gri */
            margin-top: 6px;
            margin-bottom: 3px;
            font-family: 'Helvetica Neue', 'Segoe UI';
        }
    """)


# Input (QLineEdit) stili (Apple flat input)
def style_input(input_field: QLineEdit):
    input_field.setFixedHeight(32)
    input_field.setStyleSheet("""
        QLineEdit {
            border: 1px solid #d1d1d6;
            border-radius: 6px;
            padding: 4px 8px;
            font-size: 10pt;
            background-color: #ffffff;
            font-family: 'Helvetica Neue', 'Segoe UI';
        }
        QLineEdit:focus {
            border: 1px solid #007aff;
            background-color: #f0f8ff;
        }
        QLineEdit:disabled {
            background-color: #f2f2f7;
            color: #8e8e93;
        }
    """)


# ComboBox stili (Apple dropdown)
def style_combo(combo: QComboBox):
    combo.setFixedHeight(32)
    combo.setStyleSheet("""
        QComboBox {
            border: 1px solid #d1d1d6;
            border-radius: 6px;
            padding: 4px 8px;
            font-size: 10pt;
            background-color: #ffffff;
            font-family: 'Helvetica Neue', 'Segoe UI';
        }
        QComboBox:focus {
            border: 1px solid #007aff;
            background-color: #f0f8ff;
        }
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        QComboBox QAbstractItemView {
            border: 1px solid #d1d1d6;
            selection-background-color: #007aff;
            selection-color: white;
        }
    """)