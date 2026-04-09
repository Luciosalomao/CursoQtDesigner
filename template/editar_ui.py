# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_editar(object):
    def setupUi(self, editar):
        if not editar.objectName():
            editar.setObjectName(u"editar")
        editar.resize(518, 283)
        self.label = QLabel(editar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 501, 31))
        self.label.setStyleSheet(u"background-color: rgb(131, 131, 131);\n"
"border-color: rgb(3, 3, 3);")
        self.label_2 = QLabel(editar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 411, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.label_2.setFont(font)
        self.label_3 = QLabel(editar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 49, 16))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(editar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 61, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(editar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 130, 61, 16))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(editar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 160, 71, 16))
        self.label_6.setFont(font1)
        self.lbl_nome = QLineEdit(editar)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(100, 60, 411, 26))
        self.lbl_nome.setFont(font1)
        self.lbl_endereco = QLineEdit(editar)
        self.lbl_endereco.setObjectName(u"lbl_endereco")
        self.lbl_endereco.setGeometry(QRect(100, 90, 411, 26))
        self.lbl_endereco.setFont(font1)
        self.lbl_profissao = QLineEdit(editar)
        self.lbl_profissao.setObjectName(u"lbl_profissao")
        self.lbl_profissao.setGeometry(QRect(100, 120, 411, 26))
        self.lbl_profissao.setFont(font1)
        self.lbl_documento = QLineEdit(editar)
        self.lbl_documento.setObjectName(u"lbl_documento")
        self.lbl_documento.setGeometry(QRect(100, 150, 411, 26))
        self.lbl_documento.setFont(font1)
        self.btn_savar = QPushButton(editar)
        self.btn_savar.setObjectName(u"btn_savar")
        self.btn_savar.setGeometry(QRect(220, 240, 81, 26))
        self.btn_savar.setFont(font1)
        self.btn_cancelar = QPushButton(editar)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(340, 240, 81, 26))
        self.btn_cancelar.setFont(font1)
        self.groupBox = QGroupBox(editar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 190, 120, 80))
        font2 = QFont()
        font2.setPointSize(10)
        self.groupBox.setFont(font2)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 20, 98, 24))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 50, 98, 24))

        self.retranslateUi(editar)

        QMetaObject.connectSlotsByName(editar)
    # setupUi

    def retranslateUi(self, editar):
        editar.setWindowTitle(QCoreApplication.translate("editar", u"Editar", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("editar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">Editar usu\u00e1rio no sistema</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("editar", u"Nome:", None))
        self.label_4.setText(QCoreApplication.translate("editar", u"Endere\u00e7o:", None))
        self.label_5.setText(QCoreApplication.translate("editar", u"Profiss\u00e3o:", None))
        self.label_6.setText(QCoreApplication.translate("editar", u"Documento:", None))
        self.lbl_nome.setPlaceholderText(QCoreApplication.translate("editar", u"Insira seu nome", None))
        self.lbl_endereco.setPlaceholderText(QCoreApplication.translate("editar", u"Insira seu endere\u00e7o", None))
        self.lbl_profissao.setPlaceholderText(QCoreApplication.translate("editar", u"Insira sua profiss\u00e3o", None))
        self.lbl_documento.setPlaceholderText(QCoreApplication.translate("editar", u"Insira seu documento", None))
        self.btn_savar.setText(QCoreApplication.translate("editar", u"Salvar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("editar", u"Cancelar", None))
        self.groupBox.setTitle(QCoreApplication.translate("editar", u"Admin", None))
        self.radioButton.setText(QCoreApplication.translate("editar", u"Sim", None))
        self.radioButton_2.setText(QCoreApplication.translate("editar", u"N\u00e3o", None))
    # retranslateUi

