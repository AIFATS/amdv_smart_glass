import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QStackedWidget, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 600, 400)

        # Set window opacity to make it transparent
        self.setWindowOpacity(0.7)  # Adjust the opacity level as needed (0.0 to 1.0)

        # Main layout
        self.main_layout = QHBoxLayout()

        # List widget for category buttons
        self.category_list = QListWidget()
        self.category_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.category_list)

        # Stacked widget for different settings pages
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Container widget for the main layout
        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)

        # Connect list widget click event
        self.category_list.currentRowChanged.connect(self.display_page)

    def add_category(self, name, widget, icon_path):
        item = QListWidgetItem(name)
        icon = QIcon(icon_path)
        item.setIcon(icon)
        self.category_list.addItem(item)
        self.stacked_widget.addWidget(widget)

    def display_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    
    # Create placeholder widgets for each category
    connections_widget = QWidget()
    connections_label = QLabel("Connections Settings")
    connections_label.setStyleSheet("color: black")  # Set text color to black
    connections_layout = QVBoxLayout()
    connections_layout.addWidget(connections_label)
    connections_widget.setLayout(connections_layout)

    sound_widget = QWidget()
    sound_label = QLabel("Sound & Vibration Settings")
    sound_label.setStyleSheet("color: black")  # Set text color to black
    sound_layout = QVBoxLayout()
    sound_layout.addWidget(sound_label)
    sound_widget.setLayout(sound_layout)

    display_widget = QWidget()
    display_label = QLabel("Display Settings")
    display_label.setStyleSheet("color: black")  # Set text color to black
    display_layout = QVBoxLayout()
    display_layout.addWidget(display_label)
    display_widget.setLayout(display_layout)

    security_widget = QWidget()
    security_label = QLabel("Biometrics & Security Settings")
    security_label.setStyleSheet("color: black")  # Set text color to black
    security_layout = QVBoxLayout()
    security_layout.addWidget(security_label)
    security_widget.setLayout(security_layout)
    
    # Add categories to the main window
    main_window.add_category("Connections", connections_widget, "File_Management/config/svg_files/Connections/wifi.svg")
    main_window.add_category("Sound & Vibration", sound_widget, "File_Management/config/svg_files/Sound_&_Vibration/sound.svg")
    main_window.add_category("Display", display_widget, "File_Management/config/svg_files/Display/display.svg")
    main_window.add_category("Biometrics & Security", security_widget, "File_Management/config/svg_files/Biometrics_&_Security/security.svg")
    
    main_window.show()
    sys.exit(app.exec_())
