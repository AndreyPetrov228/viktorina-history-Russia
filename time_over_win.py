from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
)

class time_over(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.connects()
        self.show()