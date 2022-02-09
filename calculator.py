from ast import Try
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculator(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px;}'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_button(QPushButton('7'), 1, 0, 1, 1)
        self.add_button(QPushButton('8'), 1, 1, 1, 1)
        self.add_button(QPushButton('9'), 1, 2, 1, 1)
        self.add_button(QPushButton('+'), 1, 3, 1, 1)
        self.add_button(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText('')
        )

        self.add_button(QPushButton('4'), 2, 0, 1, 1)
        self.add_button(QPushButton('5'), 2, 1, 1, 1)
        self.add_button(QPushButton('6'), 2, 2, 1, 1)
        self.add_button(QPushButton('-'), 2, 3, 1, 1)
        self.add_button(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(self.display.text()[:-1])
        )

        self.add_button(QPushButton('1'), 3, 0, 1, 1)
        self.add_button(QPushButton('2'), 3, 1, 1, 1)
        self.add_button(QPushButton('3'), 3, 2, 1, 1)
        self.add_button(QPushButton('/'), 3, 3, 1, 1)
        self.add_button(QPushButton(''), 3, 4, 1, 1)

        self.add_button(QPushButton('.'), 4, 0, 1, 1)
        self.add_button(QPushButton('0'), 4, 1, 1, 1)
        self.add_button(QPushButton(''), 4, 2, 1, 1)
        self.add_button(QPushButton('*'), 4, 3, 1, 1)
        self.add_button(QPushButton('='), 4, 4, 1, 1,
            lambda: self.display.setText(
                self.eval_expression(self.display.text())
            )
        )

        self.setCentralWidget(self.cw)

    def add_button(self, button:QPushButton, row, col, rowspan, colspan, func = None, style = None):
        self.grid.addWidget(button, row, col, rowspan, colspan)
        if style:
            button.setStyleSheet(style)

        if not func:
            button.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + button.text()
                )
            )
        else:
            button.clicked.connect(func)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_expression(self, expression:str):
        result = ''
        try:
            result = eval(expression)
        except:
            result = "Invalid account."
        return str(result)

        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()