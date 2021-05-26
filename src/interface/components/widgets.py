from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QFrame, QLineEdit, QComboBox
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QImage, QPixmap


PURPLE = '#28002e'
YELLOW = '#dfb300'
ORANGE = '#d35400'


class Label(QLabel):
    def __init__(self, label: str, *args, **kwargs):
        super().__init__(label, *args, **kwargs)
        self.setStyleSheet(f"""
            color:white;
            font-size:18px;
        """)


class Button(QPushButton):
    def __init__(self, label: str, callback_func: object, *args, **kwargs):
        super().__init__(label, *args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(f"""
            *{{
            color:{PURPLE};
            background-color:{YELLOW};
            font-size:20px;
            border:1px solid {YELLOW};
            border-radius:16;
            padding:6px 10px;
            }}
            *:hover{{
                background-color:white;
                border-color:white;
            }}
        """)
        self.clicked.connect(callback_func)


class Entry(QLineEdit):
    def __init__(self, placeholder: str = ' ', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet(f"""
            * {{
            color:{PURPLE};
            background-color:{YELLOW};
            padding:4px 5px;
            font-size:20px;
            border-radius:14;
            }}
            *:hover{{
                background-color:white;
            }}
            
        """)


class Combobox(QComboBox):
    def __init__(self, initial_items: tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addItems(initial_items)
        self.setStyleSheet(f"""
            * {{
            color:{PURPLE};
            background-color:{YELLOW};
            padding:4px 5px;
            font-size:20px;
            border-radius:14;
            }}
            *:hover{{
                background-color:white;
            }}
            
        """)
