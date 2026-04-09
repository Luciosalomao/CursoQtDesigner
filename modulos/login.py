from PySide6.QtWidgets import QDialog, QMessageBox
from template.login_ui import Ui_login
from modulos.principal import principal
class Login(QDialog):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.btn_entrar.clicked.connect(self.login)

    def login(self):
        admin = "admin"
        senha = "admin"
        user = ""
        password = ""
        user = self.ui.edt_user.text()
        password = self.ui.edt_pwd.text()
        if (user == admin and password == senha):
            QMessageBox.information(self,"Login realizado!", "Conectado com sucesso!")
            self.window = principal(usuario_logado=user)
            self.window.show()
            self.close()
        else:
            QMessageBox.information(self,"Falha no login!", "Desconectado!")

