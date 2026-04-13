import hashlib

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMessageBox
from template.caduser_ui import Ui_frmCadastroUsuario
from db.query import sqlite_db


class CadUser(QDialog):
    def __init__(self, *args, **kwargs):
        super(CadUser, self).__init__(*args, **kwargs)
        icon = QIcon("icones/security2.ico")
        self.setWindowIcon(icon)
        self.ui = Ui_frmCadastroUsuario()
        self.ui.setupUi(self)
        self.ui.btmCadastrar.clicked.connect(self.inserir)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnApagar.clicked.connect(self.apagar)
        self.ui.btnPesquisar.clicked.connect(self.pesquisar)
        self.ui.btnAtualizar.clicked.connect(self.atualizar)

    def criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def inserir(self):
        nom = self.ui.edt_user.text().strip()
        pwd = self.ui.edt_pwd.text().strip()

        if not nom:
            QMessageBox.warning(self, "Aviso", "Digite o nome do usuário!")
            self.ui.edt_user.setFocus()
            return

        if not pwd:
            QMessageBox.warning(self, "Aviso", "Digite a senha!")
            self.ui.edt_pwd.setFocus()
            return

        senha_criptografada = self.criptografar_senha(pwd)

        db = sqlite_db()

        campos_usuarios = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'usuario': 'TEXT UNIQUE NOT NULL',
            'senha': 'TEXT NOT NULL',
            'data_criacao': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
        }
        db.criar_tabela('usuarios', campos_usuarios)

        dados = {
            'usuario': nom,
            'senha': senha_criptografada,
        }

        resultado = db.insert("usuarios", dados)

        if resultado:
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.limpar()
        else:
            QMessageBox.warning(self, "Erro", "Falha ao cadastrar usuário!\nVerifique se o usuário já existe.")

        db.close()

    def cancelar(self):
        resposta = QMessageBox.question(self, "Confirmar", "Deseja realmente cancelar?",
                                        QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            self.close()

    def limpar(self):
        self.ui.edt_user.clear()
        self.ui.edt_pwd.clear()
        self.ui.edt_user.setFocus()

    def apagar(self):
        user = self.ui.edt_user.text().strip()

        if not user:
            QMessageBox.warning(self, "Aviso", "Digite o nome do usuário que deseja apagar!")
            self.ui.edt_user.setFocus()
            return

        resposta = QMessageBox.question(self, "Confirmar", f"Deseja realmente apagar o usuário '{user}'?",
                                        QMessageBox.Yes | QMessageBox.No)

        if resposta == QMessageBox.Yes:
            db = sqlite_db()

            resultado = db.delete("usuarios", "usuario = ?", (user,))

            db.close()

            if resultado:
                QMessageBox.information(self, "Sucesso", f"Usuário '{user}' apagado com sucesso!")
                self.limpar()
            else:
                QMessageBox.warning(self, "Erro",
                                    f"Falha ao apagar o usuário '{user}'!\nVerifique se o usuário existe.")

    def pesquisar(self):
        user = self.ui.edt_user.text().strip()

        if not user:
            QMessageBox.warning(self, "Aviso", "Digite o nome do usuário que deseja pesquisar!")
            self.ui.edt_user.setFocus()
            return

        db = sqlite_db()

        resultado = db.select("usuarios", where="usuario = ?", params=(user,))

        db.close()

        if resultado:
            usuario = resultado[0]
            self.ui.edt_user.setText(usuario[1])
            self.ui.edt_pwd.setText("********")
            QMessageBox.information(self, "Usuário Encontrado",
                                    f"Usuário: {usuario[1]}\nID: {usuario[0]}\nData de Criação: {usuario[3]}")
        else:
            QMessageBox.warning(self, "Erro", f"Usuário '{user}' não encontrado!")
            self.limpar()

    def cancelar(self):
        resposta = QMessageBox.question(self, "Confirmar", "Deseja realmente cancelar?",
                                        QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            self.close()

    def atualizar(self):
        user = self.ui.edt_user.text().strip()
        new_password = self.ui.edt_pwd.text().strip()

        if not user:
            QMessageBox.warning(self, "Aviso", "Digite o nome do usuário que deseja atualizar!")
            self.ui.edt_user.setFocus()
            return

        if not new_password:
            QMessageBox.warning(self, "Aviso", "Digite a nova senha!")
            self.ui.edt_pwd.setFocus()
            return

        if user.lower() == 'admin' and new_password:
            resposta = QMessageBox.question(self, "Confirmar", f"Deseja realmente alterar a senha do usuário 'admin'?",
                                            QMessageBox.Yes | QMessageBox.No)
            if resposta != QMessageBox.Yes:
                return

        resposta = QMessageBox.question(self, "Confirmar", f"Deseja realmente atualizar a senha do usuário '{user}'?",
                                        QMessageBox.Yes | QMessageBox.No)

        if resposta == QMessageBox.Yes:
            senha_criptografada = self.criptografar_senha(new_password)

            db = sqlite_db()

            dados = {
                'senha': senha_criptografada
            }

            resultado = db.update("usuarios", dados, "usuario = ?", (user,))

            db.close()

            if resultado:
                QMessageBox.information(self, "Sucesso", f"Senha do usuário '{user}' atualizada com sucesso!")
                self.limpar()
            else:
                QMessageBox.warning(self, "Erro",
                                    f"Falha ao atualizar a senha do usuário '{user}'!\nVerifique se o usuário existe.")