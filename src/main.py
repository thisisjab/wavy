from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
import logging


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
