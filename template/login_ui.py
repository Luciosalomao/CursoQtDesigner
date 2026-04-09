# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(385, 282)
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 381, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.lbl_user = QLabel(login)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setGeometry(QRect(60, 75, 49, 16))
        self.lbl_user.setFont(font)
        self.lbl_user.setStyleSheet(u"")
        self.lbl_pwd = QLabel(login)
        self.lbl_pwd.setObjectName(u"lbl_pwd")
        self.lbl_pwd.setGeometry(QRect(60, 121, 41, 20))
        self.lbl_pwd.setFont(font)
        self.lbl_msg = QLabel(login)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setGeometry(QRect(10, 250, 161, 31))
        self.lbl_msg.setFont(font)
        self.edt_user = QLineEdit(login)
        self.edt_user.setObjectName(u"edt_user")
        self.edt_user.setGeometry(QRect(110, 70, 211, 26))
        self.edt_user.setFont(font)
        self.edt_pwd = QLineEdit(login)
        self.edt_pwd.setObjectName(u"edt_pwd")
        self.edt_pwd.setGeometry(QRect(110, 120, 211, 26))
        self.edt_pwd.setFont(font)
        self.edt_pwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_entrar = QPushButton(login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(60, 190, 81, 26))
        self.btn_entrar.setFont(font)
        self.btn_sair = QPushButton(login)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(240, 190, 81, 26))
        self.btn_sair.setFont(font)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Login", None))
        self.label.setText(QCoreApplication.translate("login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#0000ff;\">SISTEMA DE CADASTRO DE FUNCION\u00c1RIOS</span></p></body></html>", None))
        self.lbl_user.setText(QCoreApplication.translate("login", u"Usu\u00e1rio:", None))
        self.lbl_pwd.setText(QCoreApplication.translate("login", u"Senha:", None))
        self.lbl_msg.setText(QCoreApplication.translate("login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#1e5405;\">Esqueceu sua senha?</span></p></body></html>", None))
        self.edt_user.setPlaceholderText(QCoreApplication.translate("login", u"Digite seu login", None))
        self.edt_pwd.setText("")
        self.edt_pwd.setPlaceholderText(QCoreApplication.translate("login", u"Digite sua senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.btn_sair.setText(QCoreApplication.translate("login", u"Sair", None))
    # retranslateUi


# ... (seu código gerado) ...

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())