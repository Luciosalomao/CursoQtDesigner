# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
                               QMenu, QMenuBar, QSizePolicy, QStatusBar,
                               QTableWidget, QTableWidgetItem, QToolBar, QWidget, QDialog)
import template.principal_rc

class Ui_principal(object):
    def setupUi(self, principal):
        if not principal.objectName():
            principal.setObjectName(u"principal")
        principal.resize(773, 600)
        self.actionProcurar = QAction(principal)
        self.actionProcurar.setObjectName(u"actionProcurar")
        icon = QIcon()
        icon.addFile(u":/icones/procurar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionProcurar.setIcon(icon)
        self.actionCadastrar = QAction(principal)
        self.actionCadastrar.setObjectName(u"actionCadastrar")
        icon1 = QIcon()
        icon1.addFile(u":/icones/inserir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCadastrar.setIcon(icon1)
        self.actionApagar = QAction(principal)
        self.actionApagar.setObjectName(u"actionApagar")
        icon2 = QIcon()
        icon2.addFile(u":/icones/apagar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionApagar.setIcon(icon2)
        self.actionAtualizar = QAction(principal)
        self.actionAtualizar.setObjectName(u"actionAtualizar")
        icon3 = QIcon()
        icon3.addFile(u":/icones/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAtualizar.setIcon(icon3)
        self.actionRefresh = QAction(principal)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon4 = QIcon()
        icon4.addFile(u":/icones/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRefresh.setIcon(icon4)
        self.centralwidget = QWidget(principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 731, 41))
        self.label.setStyleSheet(u"background-color: rgb(130, 130, 130);\n"
"border-color: rgb(66, 66, 66);")
        self.label.setLineWidth(1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 221, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 39, 101, 16))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        self.label_3.setFont(font1)
        self.lbl_logado = QLabel(self.centralwidget)
        self.lbl_logado.setObjectName(u"lbl_logado")
        self.lbl_logado.setGeometry(QRect(600, 40, 49, 16))
        self.lbl_logado.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 80, 731, 192))
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnHidden(0, True)
        principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 773, 33))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(principal)
        self.statusbar.setObjectName(u"statusbar")
        principal.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(principal)
        self.toolBar.setObjectName(u"toolBar")
        principal.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionProcurar)
        self.menuArquivo.addAction(self.actionCadastrar)
        self.menuArquivo.addAction(self.actionApagar)
        self.menuArquivo.addAction(self.actionAtualizar)
        self.menuArquivo.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionProcurar)
        self.toolBar.addAction(self.actionCadastrar)
        self.toolBar.addAction(self.actionApagar)
        self.toolBar.addAction(self.actionAtualizar)
        self.toolBar.addAction(self.actionRefresh)

        self.retranslateUi(principal)

        QMetaObject.connectSlotsByName(principal)
    # setupUi

    def retranslateUi(self, principal):
        principal.setWindowTitle(QCoreApplication.translate("principal", u"Principal", None))
        self.actionProcurar.setText(QCoreApplication.translate("principal", u"Procurar", None))
        self.actionCadastrar.setText(QCoreApplication.translate("principal", u"Cadastrar", None))
        self.actionApagar.setText(QCoreApplication.translate("principal", u"Apagar", None))
        self.actionAtualizar.setText(QCoreApplication.translate("principal", u"Atualizar", None))
        self.actionRefresh.setText(QCoreApplication.translate("principal", u"Refresh", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh.setShortcut(QCoreApplication.translate("principal", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">USU\u00c1RIOS CADASTRADOS</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("principal", u"<html><head/><body><p><span style=\" font-weight:700;\">Usu\u00e1rio Logado:</span></p></body></html>", None))
        self.lbl_logado.setText(QCoreApplication.translate("principal", u"...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("principal", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("principal", u"Endere\u00e7o", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("principal", u"Profiss\u00e3o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("principal", u"Documento", None));
        self.menuArquivo.setTitle(QCoreApplication.translate("principal", u"Arquivo", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("principal", u"toolBar", None))
    # retranslateUi

class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_principal()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = PrincipalWindow()
    window.show()

    sys.exit(app.exec())