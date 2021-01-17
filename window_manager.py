from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout
from PySide6.QtCore import Slot
from calculator import calculator

BTN_NAMES = ['%', 'CE', 'C', '←',
            '1/x', 'x²', 'r2', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '=']

class window_manager(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()

        self.display = QLabel("0")
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        self.btns = []
        for i in range(0, len(BTN_NAMES)):
            row = int(i/4)+1
            column = i%4
            self.btns.append(QPushButton(BTN_NAMES[i]))
            self.btns[i].clicked.connect(self.btn_clicked)
            self.layout.addWidget(self.btns[i], row, column)

        self.setLayout(self.layout)

        self.cal = calculator()

    def change_display(self, display_text):
        self.display.setText(display_text)

    @Slot()
    def btn_clicked(self):
        user_input = self.sender().text()
        self.cal.update(user_input)

        self.change_display(self.cal.user_input)