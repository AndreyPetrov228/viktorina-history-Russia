from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
)

class CategoryWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.connects()
        self.show()

    def initUI(self):
        # Настройка главного окна
        self.setWindowTitle('Выбор категории')
        self.setGeometry(300, 300, 550, 300)

        # Главный ВЕРТИКАЛЬНЫЙ слой (основа)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(30)  # Расстояние между горизонтальными рядами
        main_layout.setContentsMargins(40, 40, 40, 40)  # Отступы от краев окна

        # --- ПЕРВЫЙ ГОРИЗОНТАЛЬНЫЙ РЯД (Заголовок) ---
        row1_layout = QHBoxLayout()
        title_label = QLabel('выберите категорию', self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        row1_layout.addWidget(title_label)
        
        main_layout.addLayout(row1_layout)


        # --- ВТОРОЙ ГОРИЗОНТАЛЬНЫЙ РЯД (3 зеленые кнопки) ---
        row2_layout = QHBoxLayout()
        row2_layout.setSpacing(15)  # Расстояние между кнопками категорий
        
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
        
        btn_90s = QPushButton('Россия 90-х', self)
        btn_00s = QPushButton('Россия 00-х', self)
        btn_10s_20s = QPushButton('Россия 10-х и 20-х', self)
        
        # Применяем зеленый стиль ко всем трем кнопкам
        btn_90s.setStyleSheet(green_button_style)
        btn_00s.setStyleSheet(green_button_style)
        btn_10s_20s.setStyleSheet(green_button_style)
        
        row2_layout.addWidget(btn_90s)
        row2_layout.addWidget(btn_00s)
        row2_layout.addWidget(btn_10s_20s)
        
        main_layout.addLayout(row2_layout)


        # --- ТРЕТИЙ ГОРИЗОНТАЛЬНЫЙ РЯД (1 красная кнопка) ---
        row3_layout = QHBoxLayout()
        
        btn_start = QPushButton('начать викторину', self)
        # Красный стиль для финальной кнопки
        btn_start.setStyleSheet("""
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
        
        row3_layout.addWidget(btn_start)
        main_layout.addLayout(row3_layout)


        # Устанавливаем главный вертикальный слой для окна
        self.setLayout(main_layout)
