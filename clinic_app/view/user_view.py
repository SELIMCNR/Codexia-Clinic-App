from PyQt6.QtWidgets import QWidget, QVBoxLayout,QSplitter, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QPushButton
from utils.theme_helper import apply_theme, style_button, style_table, style_label,style_combo,style_input,tighten_layout


from PyQt6.QtCore import Qt
class UserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Management")
        self.init_ui()
        apply_theme(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setMinimumSize(1024, 768)
    def init_ui(self):
        # Sol taraf (kullanıcı listesi)
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Username", "Role"])
        self.table.setSelectionBehavior(self.table.SelectionBehavior.SelectRows)
        style_table(self.table)

        table_layout = QVBoxLayout()
        tighten_layout(table_layout)
        table_layout.addWidget(QLabel("User List"))
        style_label(table_layout.itemAt(table_layout.count()-1).widget())
        table_layout.addWidget(self.table)

        table_widget = QWidget()
        table_widget.setLayout(table_layout)

        # Sağ taraf (işlem paneli)
        panel_layout = QVBoxLayout()
        tighten_layout(panel_layout)

        panel_layout.addWidget(QLabel("Change Role"))
        style_label(panel_layout.itemAt(panel_layout.count()-1).widget())
        self.role_combo = QComboBox()
        self.role_combo.addItems(["Admin", "Doctor", "Secretary"])
        style_combo(self.role_combo)
        panel_layout.addWidget(self.role_combo)

        self.update_role_button = QPushButton("Update Role")
        style_button(self.update_role_button)
        panel_layout.addWidget(self.update_role_button)

        panel_layout.addWidget(QLabel("Reset Password"))
        style_label(panel_layout.itemAt(panel_layout.count()-1).widget())
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("New Password")
        style_input(self.password_input)
        panel_layout.addWidget(self.password_input)

        self.reset_password_button = QPushButton("Reset Password")
        style_button(self.reset_password_button)
        panel_layout.addWidget(self.reset_password_button)

        panel_widget = QWidget()
        panel_widget.setLayout(panel_layout)

        # QSplitter ile responsive görünüm
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(table_widget)
        splitter.addWidget(panel_widget)
        splitter.setSizes([600, 400])  # başlangıçta tablo geniş, panel dar

        # Ana layout
        main_layout = QVBoxLayout()
        tighten_layout(main_layout)
        main_layout.addWidget(QLabel("User Management"))
        style_label(main_layout.itemAt(main_layout.count()-1).widget())
        main_layout.addWidget(splitter)

        self.setLayout(main_layout)