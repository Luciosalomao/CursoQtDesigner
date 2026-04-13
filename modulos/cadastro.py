from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMessageBox
from template.cadastro_ui import Ui_cadastro
from db.query import sqlite_db


class Cadastro(QDialog):
    def __init__(self, *args, **kwargs):
        super(Cadastro, self).__init__(*args, **kwargs)
        icon = QIcon("icones/security2.png")
        self.setWindowIcon(icon)
        self.ui = Ui_cadastro()
        self.ui.setupUi(self)
        self.ui.btn_cadastrar.clicked.connect(self.inserir)
        self.ui.btn_limpar.clicked.connect(self.limpar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def inserir(self):
        nom = self.ui.lineEdit.text().strip()
        end = self.ui.lineEdit_2.text().strip()
        pro = self.ui.lineEdit_3.text().strip()
        doc = self.ui.lineEdit_4.text().strip()

        if not nom:
            QMessageBox.warning(self, "Aviso", "Digite o nome do funcionario!")
            self.ui.lineEdit.setFocus()
            return

        db = sqlite_db()

        campos_funcionarios = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'endereco': 'TEXT',
            'profissao': 'TEXT',
            'documento': 'TEXT',
            'admin': 'INTEGER DEFAULT 0'
        }

        db.criar_tabela('funcionarios', campos_funcionarios)

        dados = {
            'nome': nom,
            'endereco': end,
            'profissao': pro,
            'documento': doc,
            'admin': 0
        }

        resultado = db.insert("funcionarios", dados)

        if resultado:
            QMessageBox.information(self, "Sucesso", "Dados gravados com sucesso!")
            self.limpar()
        else:
            QMessageBox.warning(self, "Erro", "Falha ao gravar os dados!\nVerifique se o documento ja existe.")

        db.close()

    def cancelar(self):
        resposta = QMessageBox.question(self, "Confirmar", "Deseja realmente cancelar?",
                                        QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            self.close()

    def limpar(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit.setFocus()