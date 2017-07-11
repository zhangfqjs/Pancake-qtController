import sys
import PyQt5
from PyQt5.QtWidgets import *

import ui_mainwindow

class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):

    current_value = 5
    max_value = 10
    min_value = 0
    value_step = 1

    def pressedOnButton(self):
        if self.current_value < self.max_value:
            self.current_value += self.value_step
        print (self.current_value)

    def pressedOffButton(self):
        if self.current_value > self.min_value:
            self.current_value -= self.value_step
        print (self.current_value)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
