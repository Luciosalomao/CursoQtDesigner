from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QComboBox, QMessageBox, QTableWidgetItem
from db.query import sqlite_db

class PesquisarFuncionario(QDialog):
    def __init__(self, parent=None):
        super(PesquisarFuncionario, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Pesquisar Funcionário")
        self.setModal(True)
        self.setMinimumWidth(400)

        self.setup_ui()

    def setup_ui(self):
        layout = QFormLayout(self)

        self.cmb_campo = QComboBox()
        self.cmb_campo.addItems(["Nome", "Documento", "Profissão", "Todos os campos"])
        layout.addRow("Pesquisar por:", self.cmb_campo)

        self.txt_pesquisar = QLineEdit()
        self.txt_pesquisar.setPlaceholderText("Digite o termo para pesquisa...")
        layout.addRow("Termo:", self.txt_pesquisar)

        btn_buscar = QPushButton("Buscar")
        btn_cancelar = QPushButton("Cancelar")
        btn_limpar = QPushButton("Limpar")

        layout.addRow(btn_buscar, btn_cancelar)
        layout.addRow(btn_limpar, QPushButton())

        btn_buscar.clicked.connect(self.executar_pesquisa)
        btn_cancelar.clicked.connect(self.reject)
        btn_limpar.clicked.connect(self.limpar_pesquisa)
        self.txt_pesquisar.returnPressed.connect(self.executar_pesquisa)

    def executar_pesquisa(self):
        termo_busca = self.txt_pesquisar.text().strip()

        if not termo_busca:
            QMessageBox.warning(self, "Atenção", "Digite um termo para pesquisa!")
            return

        db = sqlite_db()
        campo = self.cmb_campo.currentText()
        termo_busca_param = f"%{termo_busca}%"

        if campo == "Nome":
            where_clause = "nome LIKE ?"
            params = (termo_busca_param,)
        elif campo == "Documento":
            where_clause = "documento LIKE ?"
            params = (termo_busca_param,)
        elif campo == "Profissão":
            where_clause = "profissao LIKE ?"
            params = (termo_busca_param,)
        else:  # Todos os campos
            where_clause = "nome LIKE ? OR documento LIKE ? OR profissao LIKE ?"
            params = (termo_busca_param, termo_busca_param, termo_busca_param)

        resultados = db.select("funcionarios",
                               campos="*",
                               where=where_clause,
                               params=params,
                               order="nome")

        db.close()

        if resultados:
            self.parent.ui.tableWidget.setRowCount(len(resultados))

            for i, func in enumerate(resultados):
                self.parent.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(func[0])))
                self.parent.ui.tableWidget.setItem(i, 1, QTableWidgetItem(func[1]))
                self.parent.ui.tableWidget.setItem(i, 2, QTableWidgetItem(func[2]))
                self.parent.ui.tableWidget.setItem(i, 3, QTableWidgetItem(func[3]))
                self.parent.ui.tableWidget.setItem(i, 4, QTableWidgetItem(func[4]))
                self.parent.ui.tableWidget.setItem(i, 5, QTableWidgetItem("Sim" if func[5] == 1 else "Não"))

            self.parent.ui.tableWidget.resizeColumnsToContents()

            QMessageBox.information(self, "Pesquisa concluída",
                                    f"Encontrados {len(resultados)} resultado(s) para: {termo_busca}")

            self.accept()
        else:
            QMessageBox.information(self, "Pesquisa",
                                    f"Nenhum funcionário encontrado com o termo: {termo_busca}")

    def limpar_pesquisa(self):
        self.txt_pesquisar.clear()
        self.txt_pesquisar.setFocus()