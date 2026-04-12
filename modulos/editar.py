from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog
from template.editar_ui import Ui_editar
class Editar(QDialog):
    def __init__(self, dados_funcionario, parent=None):
        super(Editar, self).__init__(parent)
        icon = QIcon("icones/security2.png")
        self.setWindowIcon(icon)
        self.ui = Ui_editar()
        self.ui.setupUi(self)

        self.id_funcionario = dados_funcionario[0]

        self.ui.lbl_nome.setText(dados_funcionario[1])
        self.ui.lbl_endereco.setText(dados_funcionario[2])
        self.ui.lbl_profissao.setText(dados_funcionario[3])
        self.ui.lbl_documento.setText(dados_funcionario[4])

        if dados_funcionario[5] == 1:  # Se for admin
            self.ui.radioButton.setChecked(True)
        else:
            self.ui.radioButton_2.setChecked(True)

        self.ui.btn_savar.clicked.connect(self.salvar)
        self.ui.btn_cancelar.clicked.connect(self.reject)

    def salvar(self):
        if not self.ui.lbl_nome.text().strip():
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "O campo Nome é obrigatório!")
            return

        self.accept()

    def get_dados_atualizados(self):
        return {
            'nome': self.ui.lbl_nome.text().strip(),
            'endereco': self.ui.lbl_endereco.text().strip(),
            'profissao': self.ui.lbl_profissao.text().strip(),
            'documento': self.ui.lbl_documento.text().strip(),
            'admin': 1 if self.ui.radioButton.isChecked() else 0
        }