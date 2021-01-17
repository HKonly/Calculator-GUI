import sys
from PySide6.QtWidgets import QApplication, QWidget
from window_manager import window_manager

app = QApplication(sys.argv)
app.setStyle("fusion")

window_manager = window_manager()

window_manager.show()

app.exec_()