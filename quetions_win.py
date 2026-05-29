from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
)

class QuestionsWin(QWidget):
    def __init__(self, question_list):
        super().__init__()
        self.question_list = question_list
        self.initUI()
        # self.connects()
        self.show()

    def initUI(self):
        pass
