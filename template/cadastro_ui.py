# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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

class Ui_cadastro(object):
    def setupUi(self, cadastro):
        if not cadastro.objectName():
            cadastro.setObjectName(u"cadastro")
        cadastro.resize(518, 284)
        self.label = QLabel(cadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 501, 31))
        self.label.setStyleSheet(u"background-color: rgb(131, 131, 131);\n"
"border-color: rgb(3, 3, 3);")
        self.label_2 = QLabel(cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 411, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.label_2.setFont(font)
        self.label_3 = QLabel(cadastro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 49, 16))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(cadastro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 61, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(cadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 130, 61, 16))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 160, 71, 16))
        self.label_6.setFont(font1)
        self.lineEdit = QLineEdit(cadastro)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 60, 411, 26))
        self.lineEdit.setFont(font1)
        self.lineEdit_2 = QLineEdit(cadastro)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 90, 411, 26))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_3 = QLineEdit(cadastro)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(100, 120, 411, 26))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_4 = QLineEdit(cadastro)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(100, 150, 411, 26))
        self.lineEdit_4.setFont(font1)
        self.btn_cadastrar = QPushButton(cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(140, 220, 81, 26))
        self.btn_cadastrar.setFont(font1)
        self.btn_cancelar = QPushButton(cadastro)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(240, 220, 81, 26))
        self.btn_cancelar.setFont(font1)
        self.btn_limpar = QPushButton(cadastro)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setGeometry(QRect(340, 220, 81, 26))
        self.btn_limpar.setFont(font1)

        self.retranslateUi(cadastro)

        QMetaObject.connectSlotsByName(cadastro)
    # setupUi

    def retranslateUi(self, cadastro):
        cadastro.setWindowTitle(QCoreApplication.translate("cadastro", u"Cadastro", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("cadastro", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">Cadastrar usu\u00e1rio no sistema</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("cadastro", u"Nome:", None))
        self.label_4.setText(QCoreApplication.translate("cadastro", u"Endere\u00e7o:", None))
        self.label_5.setText(QCoreApplication.translate("cadastro", u"Profiss\u00e3o:", None))
        self.label_6.setText(QCoreApplication.translate("cadastro", u"Documento:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("cadastro", u"Insira seu nome", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("cadastro", u"Insira seu endere\u00e7o", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("cadastro", u"Insira sua profiss\u00e3o", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("cadastro", u"Insira seu documento", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("cadastro", u"Cadastrar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("cadastro", u"Cancelar", None))
        self.btn_limpar.setText(QCoreApplication.translate("cadastro", u"Limpar", None))
    # retranslateUi

class CadastroWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_cadastro()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = CadastroWindow()
    window.show()

    sys.exit(app.exec())