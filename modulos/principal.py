from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QDialog, QFormLayout, QLineEdit, QPushButton

from modulos.pesquisar_funcionario import PesquisarFuncionario
from template.principal_ui import Ui_principal
from modulos.cadastro import Cadastro
from db.query import sqlite_db
from modulos.editar import Editar
from modulos.caduser import CadUser

class principal(QMainWindow):
    def __init__(self, usuario_logado=None, *args, **kwargs):
        super(principal, self).__init__(*args, **kwargs)
        self.ui = Ui_principal()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.inserir)
        self.ui.actionApagar.triggered.connect(self.apagar_registro)
        self.ui.actionAtualizar.triggered.connect(self.atualizar_registro)
        self.ui.actionRefresh.triggered.connect(self.carregar_dados)
        self.ui.actionProcurar.triggered.connect(self.pesquisar_funcionario)
        self.ui.actionCadastrar_user.triggered.connect(self.caduser)
        if usuario_logado:
            self.ui.lbl_logado.setText(
                f'<html><head/><body><p><span style=" color:#00ff00; font-weight:700;">{usuario_logado}</span></p></body></html>'
            )
        else:
            self.ui.lbl_logado.setText("Não logado")
        self.carregar_dados()

    def pesquisar_funcionario(self):
        pesquisar_dialog = PesquisarFuncionario(self)
        pesquisar_dialog.exec_()

    def inserir(self):
        inserir = Cadastro()
        inserir.exec_()
        self.carregar_dados()

    def carregar_dados(self):
        db = sqlite_db()

        funcionarios = db.select("funcionarios")

        if funcionarios:
            self.ui.tableWidget.setRowCount(len(funcionarios))
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "Endereço", "Profissão", "Documento", "Admin"])

            for i, func in enumerate(funcionarios):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(func[0])))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(func[1]))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(func[2]))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(func[3]))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(func[4]))
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem("Sim" if func[5] == 1 else "Não"))

            self.ui.tableWidget.resizeColumnsToContents()
        else:
            self.ui.tableWidget.setRowCount(0)

        db.close()

    def apagar_registro(self):
        linha_selecionada = self.ui.tableWidget.currentRow()

        if linha_selecionada == -1:
            QMessageBox.warning(self, "Atenção", "Selecione um registro para apagar!")
            return

        id_registro = self.ui.tableWidget.item(linha_selecionada, 0).text()
        nome_registro = self.ui.tableWidget.item(linha_selecionada, 1).text()

        resposta = QMessageBox.question(
            self,
            "Confirmar",
            f"Tem certeza que deseja apagar o registro:\nID: {id_registro}\nNome: {nome_registro}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta == QMessageBox.Yes:
            db = sqlite_db()
            resultado = db.delete("funcionarios", "id = ?", (id_registro,))
            db.close()

            if resultado:
                QMessageBox.information(self, "Sucesso", "Registro apagado com sucesso!")
                self.carregar_dados()
            else:
                QMessageBox.critical(self, "Erro", "Erro ao apagar o registro!")

    def atualizar_registro(self):
        linha_selecionada = self.ui.tableWidget.currentRow()

        if linha_selecionada == -1:
            QMessageBox.warning(self, "Atenção", "Selecione um registro para atualizar!")
            return

        id_registro = self.ui.tableWidget.item(linha_selecionada, 0).text()
        nome_atual = self.ui.tableWidget.item(linha_selecionada, 1).text()
        endereco_atual = self.ui.tableWidget.item(linha_selecionada, 2).text()
        profissao_atual = self.ui.tableWidget.item(linha_selecionada, 3).text()
        documento_atual = self.ui.tableWidget.item(linha_selecionada, 4).text()
        admin_atual = 1 if self.ui.tableWidget.item(linha_selecionada, 5).text() == "Sim" else 0

        dados_funcionario = (id_registro, nome_atual, endereco_atual,
                             profissao_atual, documento_atual, admin_atual)

        dialog = Editar(dados_funcionario, self)

        if dialog.exec() == QDialog.Accepted:
            dados_atualizados = dialog.get_dados_atualizados()

            db = sqlite_db()
            resultado = db.update("funcionarios", dados_atualizados, "id = ?", (id_registro,))
            db.close()

            if resultado:
                QMessageBox.information(self, "Sucesso", "Registro atualizado com sucesso!")
                self.carregar_dados()  # Recarrega a tabela
            else:
                QMessageBox.critical(self, "Erro", "Erro ao atualizar o registro!")

    def caduser(self):
        caduser = CadUser()
        caduser.exec_()
