from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
)

from category_win import CategoryWin

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.current_question = 0
        self.score = 0
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        # Настройка главного окна
        self.setWindowTitle('Викторина на PyQt5')
        self.setGeometry(300, 300, 400, 300)
        self.main_layout = QVBoxLayout()
        # Задаем отступы между элементами по вертикали
        self.main_layout.setSpacing(15)
        # Задаем внутренние отступы от краев окна (влево, вверх, вправо, вниз)
        self.main_layout.setContentsMargins(30, 30, 30, 30)

        # 1. Первая надпись
        self.label_title = QLabel('история современной России', self)
        self.label_title.setAlignment(Qt.AlignCenter) # Выравнивание по центру
        self.label_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        self.main_layout.addWidget(self.label_title)

        # 2. Вторая надпись
        self.label_subtitle = QLabel('викторина', self)
        self.label_subtitle.setAlignment(Qt.AlignCenter) # Выравнивание по центру
        self.label_subtitle.setStyleSheet("font-size: 16px; color: #7f8c8d; font-style: italic;")
        self.main_layout.addWidget(self.label_subtitle)

        # 3. Кнопка
        self.btn_category = QPushButton('перейти к выбору категории', self)


        # Красиво оформляем кнопку с помощью стилей
        self.btn_category.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 10px;
                background-color: #3498db;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.main_layout.addWidget(self.btn_category)

        # Устанавливаем вертикальный слой как главный для окна
        self.setLayout(self.main_layout)

    def next_click(self):
        self.categoryw = CategoryWin()
        self.hide()

    def connects(self):
        self.btn_category.clicked.connect(self.next_click)




app = QApplication([])
mw = MainWindow()
app.exec_()
