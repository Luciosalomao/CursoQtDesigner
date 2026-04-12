import hashlib
from PySide6.QtWidgets import QDialog, QMessageBox
from template.login_ui import Ui_login
from db.query import sqlite_db
from modulos.principal import principal


class Login(QDialog):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.btn_entrar.clicked.connect(self.login)
        self.verificar_criar_admin()

    def criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def verificar_criar_admin(self):
        db = sqlite_db()

        campos_usuarios = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'usuario': 'TEXT UNIQUE NOT NULL',
            'senha': 'TEXT NOT NULL',
            'data_criacao': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
        }
        db.criar_tabela('usuarios', campos_usuarios)

        usuarios = db.select("usuarios")

        if not usuarios:
            senha_admin = self.criptografar_senha("admin")
            dados = {
                'usuario': 'admin',
                'senha': senha_admin
            }
            db.insert("usuarios", dados)
            QMessageBox.information(self, "Admin criado",
                                    "Usuário admin criado com sucesso!\nUsuário: admin\nSenha: admin")

        db.close()

    def login(self):
        user = self.ui.edt_user.text().strip()
        password = self.ui.edt_pwd.text().strip()

        if not user:
            QMessageBox.warning(self, "Aviso", "Digite o usuário!")
            self.ui.edt_user.setFocus()
            return

        if not password:
            QMessageBox.warning(self, "Aviso", "Digite a senha!")
            self.ui.edt_pwd.setFocus()
            return

        senha_criptografada = self.criptografar_senha(password)

        db = sqlite_db()

        resultado = db.select(
            "usuarios",
            where='usuario = ? AND senha = ?',
            params=(user, senha_criptografada)
        )

        db.close()

        if resultado:
            QMessageBox.information(self, "Login realizado!", "Conectado com sucesso!")
            self.window = principal(usuario_logado=user)
            self.window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Falha no login!", "Usuário ou senha inválidos!")