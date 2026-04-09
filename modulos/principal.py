from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QDialog, QFormLayout, QLineEdit, QPushButton
from template.principal_ui import Ui_principal
from modulos.cadastro import Cadastro
from db.query import sqlite_db


class principal(QMainWindow):
    def __init__(self, usuario_logado=None, *args, **kwargs):
        super(principal, self).__init__(*args, **kwargs)
        self.ui = Ui_principal()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.inserir)
        self.ui.actionApagar.triggered.connect(self.apagar_registro)
        self.ui.actionAtualizar.triggered.connect(self.atualizar_registro)
        if usuario_logado:
            self.ui.lbl_logado.setText(f"{usuario_logado}")
        else:
            self.ui.lbl_logado.setText("Não logado")
        self.carregar_dados()

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
        admin_atual = self.ui.tableWidget.item(linha_selecionada, 5).text()

        dialog = QDialog(self)
        dialog.setWindowTitle(f"Atualizar Registro - ID: {id_registro}")
        dialog.setModal(True)

        layout = QFormLayout()

        nome_input = QLineEdit(nome_atual)
        endereco_input = QLineEdit(endereco_atual)
        profissao_input = QLineEdit(profissao_atual)
        documento_input = QLineEdit(documento_atual)

        layout.addRow("Nome:", nome_input)
        layout.addRow("Endereço:", endereco_input)
        layout.addRow("Profissão:", profissao_input)
        layout.addRow("Documento:", documento_input)

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(dialog.accept)
        layout.addRow(btn_salvar)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            novo_nome = nome_input.text().strip()
            novo_endereco = endereco_input.text().strip()
            nova_profissao = profissao_input.text().strip()
            novo_documento = documento_input.text().strip()

            if not novo_nome or not novo_endereco or not nova_profissao or not novo_documento:
                QMessageBox.warning(self, "Atenção", "Preencha todos os campos!")
                return

            db = sqlite_db()

            dados = {
                'nome': novo_nome,
                'endereco': novo_endereco,
                'profissao': nova_profissao,
                'documento': novo_documento
            }

            resultado = db.update("funcionarios", dados, "id = ?", (id_registro,))
            db.close()

            if resultado:
                QMessageBox.information(self, "Sucesso", "Registro atualizado com sucesso!")
                self.carregar_dados()
            else:
                QMessageBox.critical(self, "Erro", "Erro ao atualizar o registro!")

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