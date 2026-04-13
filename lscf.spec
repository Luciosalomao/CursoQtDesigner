import os
import sys

# Verifica se o ícone existe
icon_path = 'icones/security2.png'
if not os.path.exists(icon_path):
    print(f"AVISO: Ícone não encontrado em {icon_path}")
    icon_path = None

a = Analysis(
    ['run.py'],  # Seu arquivo principal é run.py
    pathex=[],  # Adicione caminhos extras se necessário: ['C:/Curso_Lucio/CursoQtDesigner']
    binaries=[],
    datas=[
        ('icones', 'icones'),
        ('db', 'db'),
        ('modulos', 'modulos'),
        ('template', 'template'),
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'sqlite3',
        'modulos.cadastro',
        'modulos.editar',
        'modulos.caduser',
        'modulos.pesquisar_funcionario',
        'db.query',
        'template.principal_ui',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'unittest',
        'pdb',
        'email',
        'http',
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SistemaCadastroFuncionario',  # Nome do executável
    debug=False,  # Mude para True se precisar debugar
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Requer UPX instalado (opcional, mas reduz tamanho)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # False = sem janela de console (modo gráfico)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,  # Usa a variável com verificação
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SistemaCadastroFuncionario'
)