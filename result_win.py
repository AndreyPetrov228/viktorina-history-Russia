from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
)

class ResultWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.connects()
        self.show()

class QuizResultApp(QWidget):
    def __init__(self, score=7):  # score — переданный балл (для примера поставим 7 из 10)
        super().__init__()
        self.score = score
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Результаты викторины')
        self.setGeometry(300, 300, 450, 250)

        # Главный ВЕРТИКАЛЬНЫЙ слой
        main_layout = QVBoxLayout()
        main_layout.setSpacing(25)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # --- ПЕРВЫЙ ГОРИЗОНТАЛЬНЫЙ РЯД (Текст оценки) ---
        row1_layout = QHBoxLayout()
        feedback_label = QLabel(self.get_feedback_text(), self)
        feedback_label.setAlignment(Qt.AlignCenter)
        feedback_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        feedback_label.setWordWrap(True)
        row1_layout.addWidget(feedback_label)
        main_layout.addLayout(row1_layout)

        # --- ВТОРОЙ ГОРИЗОНТАЛЬНЫЙ РЯД (Вывод баллов) ---
        row2_layout = QHBoxLayout()
        score_label = QLabel(f"Ваш результат: {self.score} из 10 баллов", self)
        score_label.setAlignment(Qt.AlignCenter)
        score_label.setStyleSheet("font-size: 16px; font-weight: 500; color: #7f8c8d;")
        row2_layout.addWidget(score_label)
        main_layout.addLayout(row2_layout)

        # --- ТРЕТИЙ ГОРИЗОНТАЛЬНЫЙ РЯД (Две зеленые кнопки) ---
        row3_layout = QHBoxLayout()
        row3_layout.setSpacing(15)

        # Стиль для зеленых кнопок
        green_btn_style = """
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """

        btn_categories = QPushButton('выбор категории', self)
        btn_categories.setStyleSheet(green_btn_style)
        
        btn_exit = QPushButton('выход', self)
        btn_exit.setStyleSheet(green_btn_style)
        
        # Привязка действия закрытия программы к кнопке "выход"
        btn_exit.clicked.connect(self.close)

        row3_layout.addWidget(btn_categories)
        row3_layout.addWidget(btn_exit)
        main_layout.addLayout(row3_layout)

        # Установка главного слоя
        self.setLayout(main_layout)

    def get_feedback_text(self):
        # Логика динамического изменения текста в зависимости от баллов
        if self.score >= 9:
            return "Отличный результат! Вы прекрасно знаете историю!"
        elif self.score >= 6:
            return "Неплохо, но вы можете лучше."
        elif self.score >= 4:
            return "Удовлетворительно. Стоит повторить материал."
        else:
            return "Попробуйте еще раз, вам нужно подтянуть знания."

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Передайте любое число от 0 до 10 в скобки, чтобы проверить разные тексты
    ex = QuizResultApp(score=7)
    ex.show()
    sys.exit(app.exec_())