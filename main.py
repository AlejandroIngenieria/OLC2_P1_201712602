import sys
from interfaz import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = Editor()
    sys.exit(app.exec_())
