# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadUser.ui'
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

class Ui_frmCadastroUsuario(object):
    def setupUi(self, frmCadastroUsuario):
        if not frmCadastroUsuario.objectName():
            frmCadastroUsuario.setObjectName(u"frmCadastroUsuario")
        frmCadastroUsuario.resize(399, 203)
        self.edt_pwd = QLineEdit(frmCadastroUsuario)
        self.edt_pwd.setObjectName(u"edt_pwd")
        self.edt_pwd.setGeometry(QRect(120, 105, 211, 26))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.edt_pwd.setFont(font)
        self.edt_pwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.edt_user = QLineEdit(frmCadastroUsuario)
        self.edt_user.setObjectName(u"edt_user")
        self.edt_user.setGeometry(QRect(120, 55, 211, 26))
        self.edt_user.setFont(font)
        self.lbl_pwd = QLabel(frmCadastroUsuario)
        self.lbl_pwd.setObjectName(u"lbl_pwd")
        self.lbl_pwd.setGeometry(QRect(70, 106, 41, 20))
        self.lbl_pwd.setFont(font)
        self.lbl_user = QLabel(frmCadastroUsuario)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setGeometry(QRect(70, 60, 49, 16))
        self.lbl_user.setFont(font)
        self.lbl_user.setStyleSheet(u"")
        self.label = QLabel(frmCadastroUsuario)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 20))
        self.label.setFont(font)
        self.btmCadastrar = QPushButton(frmCadastroUsuario)
        self.btmCadastrar.setObjectName(u"btmCadastrar")
        self.btmCadastrar.setGeometry(QRect(0, 160, 81, 26))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.btmCadastrar.setIcon(icon)
        self.btnCancelar = QPushButton(frmCadastroUsuario)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(320, 160, 81, 26))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ProcessStop))
        self.btnCancelar.setIcon(icon1)
        self.btnPesquisar = QPushButton(frmCadastroUsuario)
        self.btnPesquisar.setObjectName(u"btnPesquisar")
        self.btnPesquisar.setGeometry(QRect(80, 160, 81, 26))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.btnPesquisar.setIcon(icon2)
        self.btnApagar = QPushButton(frmCadastroUsuario)
        self.btnApagar.setObjectName(u"btnApagar")
        self.btnApagar.setGeometry(QRect(240, 160, 81, 26))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.btnApagar.setIcon(icon3)
        self.btnAtualizar = QPushButton(frmCadastroUsuario)
        self.btnAtualizar.setObjectName(u"btnAtualizar")
        self.btnAtualizar.setGeometry(QRect(160, 160, 81, 26))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.btnAtualizar.setIcon(icon4)

        self.retranslateUi(frmCadastroUsuario)

        QMetaObject.connectSlotsByName(frmCadastroUsuario)
    # setupUi

    def retranslateUi(self, frmCadastroUsuario):
        frmCadastroUsuario.setWindowTitle(QCoreApplication.translate("frmCadastroUsuario", u"Cadastro Usuario", None))
        self.edt_pwd.setText("")
        self.edt_pwd.setPlaceholderText(QCoreApplication.translate("frmCadastroUsuario", u"Digite sua senha", None))
        self.edt_user.setPlaceholderText(QCoreApplication.translate("frmCadastroUsuario", u"Digite seu login", None))
        self.lbl_pwd.setText(QCoreApplication.translate("frmCadastroUsuario", u"Senha:", None))
        self.lbl_user.setText(QCoreApplication.translate("frmCadastroUsuario", u"Usu\u00e1rio:", None))
        self.label.setText(QCoreApplication.translate("frmCadastroUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#0000ff;\">CADASTRO DE USU\u00c1RIOS</span></p></body></html>", None))
        self.btmCadastrar.setText(QCoreApplication.translate("frmCadastroUsuario", u"Cadastrar", None))
        self.btnCancelar.setText(QCoreApplication.translate("frmCadastroUsuario", u"Cancelar", None))
        self.btnPesquisar.setText(QCoreApplication.translate("frmCadastroUsuario", u"Pesquisar", None))
        self.btnApagar.setText(QCoreApplication.translate("frmCadastroUsuario", u"Apagar", None))
        self.btnAtualizar.setText(QCoreApplication.translate("frmCadastroUsuario", u"Atualizar", None))
    # retranslateUi

