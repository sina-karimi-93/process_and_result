import sys
from src.interface import QApplication, QMainWindow
from src.interface import MainFrame


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(0, 0, 1300, 680)
        self.setCentralWidget(MainFrame())
        self.setFixedHeight(790)
        self.setFixedWidth(1300)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
