from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
)

from questions import question_list

class CategoryWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.filtered_questions = []
        # self.connects()
        self.show()
 
    def create_cuetion_list_90(self):
        for q in question_list:
        # 3. Проверяем условие интервала лет внутри цикла
            if 1991 <= q["year"] <= 2001:
            # 4. Добавляем элемент в новый список
                self.filtered_questions.append(q)
        print(self.filtered_questions)
    
    def create_cuetion_list_00(self):
        for q in question_list:
        # 3. Проверяем условие интервала лет внутри цикла
            if 2002 <= q["year"] <= 2011:
            # 4. Добавляем элемент в новый список
                self.filtered_questions.append(q)
        print(self.filtered_questions)

    def create_cuetion_list_10_20(self):
        for q in question_list:
        # 3. Проверяем условие интервала лет внутри цикла
            if 2012 <= q["year"] <= 2021:
            # 4. Добавляем элемент в новый список
                self.filtered_questions.append(q)
        print(self.filtered_questions)

    def start_quise(self):
        self.question_win = QuestionsWin(self.filtered_questions)
        self.hide()

    def initUI(self):
        # Настройка главного окна
        self.setWindowTitle('Выбор категории')
        self.setGeometry(300, 300, 550, 300)

        # Главный ВЕРТИКАЛЬНЫЙ слой (основа)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(30)  # Расстояние между горизонтальными рядами
        self.main_layout.setContentsMargins(40, 40, 40, 40)  # Отступы от краев окна

        # --- ПЕРВЫЙ ГОРИЗОНТАЛЬНЫЙ РЯД (Заголовок) ---
        self.row1_layout = QHBoxLayout()
        self.title_label = QLabel('выберите категорию', self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        self.row1_layout.addWidget(self.title_label)
        self.main_layout.addLayout(self.row1_layout)


        # --- ВТОРОЙ ГОРИЗОНТАЛЬНЫЙ РЯД (3 зеленые кнопки) ---
        self.row2_layout = QHBoxLayout()
        self.row2_layout.setSpacing(15)  # Расстояние между кнопками категорий
        
        # Общий стиль для зеленых кнопок (эффект при наведении включен)
        green_button_style = """
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 6px;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """
        
        self.btn_90s = QPushButton('Россия 90-х', self)
        self.btn_00s = QPushButton('Россия 00-х', self)
        self.btn_10s_20s = QPushButton('Россия 10-х и 20-х', self)
        #8888888888888888888888888888888888888888888

        self.btn_90s.clicked.connect(self.create_cuetion_list_90)
        self.btn_00s.clicked.connect(self.create_cuetion_list_00)
        self.btn_10s_20s.clicked.connect(self.create_cuetion_list_10_20)
        
        # Применяем зеленый стиль ко всем трем кнопкам
        self.btn_90s.setStyleSheet(green_button_style)
        self.btn_00s.setStyleSheet(green_button_style)
        self.btn_10s_20s.setStyleSheet(green_button_style)
        
        self.row2_layout.addWidget(self.btn_90s)
        self.row2_layout.addWidget(self.btn_00s)
        self.row2_layout.addWidget(self.btn_10s_20s)
        
        self.main_layout.addLayout(self.row2_layout)


        # --- ТРЕТИЙ ГОРИЗОНТАЛЬНЫЙ РЯД (1 красная кнопка) ---
        self.row3_layout = QHBoxLayout()
        
        self.btn_start = QPushButton('начать викторину', self)
        self.btn_start.clicked.connect(self.start_quise)
        # Красный стиль для финальной кнопки
        self.btn_start.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 6px;
                padding: 14px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        self.row3_layout.addWidget(self.btn_start)
        self.main_layout.addLayout(self.row3_layout)


        # Устанавливаем главный вертикальный слой для окна
        self.setLayout(self.main_layout)
