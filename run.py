import sys
from PySide6.QtWidgets import QApplication, QDialog
from modulos.login import Login

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = Login()
    window.show()

sys.exit(app.exec())
