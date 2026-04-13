import sqlite3
import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


class sqlite_db:
    def __init__(self, banco=None):
        self.conn = None
        self.cursor = None

        # Se um banco específico foi passado, usa ele
        if banco is not None:
            self.banco_nome = banco
        else:
            # Pega as configurações do .env
            db_name = os.getenv('DB_NAME', 'database.db')
            db_path = os.getenv('DB_PATH', '')

            # Verifica se é para usar a mesma pasta do executável
            if db_path == '.':
                # Usa a pasta atual (onde o programa está sendo executado)
                pasta_db = os.getcwd()
                os.makedirs(pasta_db, exist_ok=True)
                self.banco_nome = os.path.join(pasta_db, db_name)
                print(f"Usando banco na pasta atual: {self.banco_nome}")

            elif db_path:
                # Caminho personalizado do .env
                pasta_db = db_path
                os.makedirs(pasta_db, exist_ok=True)
                self.banco_nome = os.path.join(pasta_db, db_name)
                print(f"Usando banco configurado no .env: {self.banco_nome}")

            else:
                # Caminho padrão (pasta db na raiz do projeto)
                raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                pasta_db = os.path.join(raiz_projeto, "db")
                os.makedirs(pasta_db, exist_ok=True)
                self.banco_nome = os.path.join(pasta_db, db_name)
                print(f"Usando banco padrao: {self.banco_nome}")

        self.open(self.banco_nome)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexao criada com sucesso!")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao conectar: {e}")
            return False

    def criar_tabela(self, nome_tabela, campos):
        """
        Cria qualquer tabela dinamicamente

        Parametros:
        - nome_tabela: nome da tabela
        - campos: dicionario com campos e tipos
        Exemplo: {'id': 'integer primary key autoincrement', 'nome': 'text', 'idade': 'integer'}
        """
        if not self.cursor:
            return False

        try:
            campos_sql = ', '.join([f"{campo} {tipo}" for campo, tipo in campos.items()])
            query = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({campos_sql})"
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Tabela '{nome_tabela}' criada/verificada com sucesso!")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
            return False

    def insert(self, tabela, dados):
        """Insere dados em qualquer tabela"""
        if not self.cursor:
            return False

        try:
            campos = ', '.join(dados.keys())
            placeholders = ', '.join(['?' for _ in dados])
            valores = list(dados.values())

            query = f"INSERT INTO {tabela} ({campos}) VALUES ({placeholders})"
            self.cursor.execute(query, valores)
            self.conn.commit()

            print(f"Inserido em '{tabela}'! ID: {self.cursor.lastrowid}")
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao inserir: {e}")
            return False

    def select(self, tabela, campos="*", where=None, params=None, order=None, limit=None):
        """Consulta qualquer tabela"""
        if not self.cursor:
            return []

        try:
            query = f"SELECT {campos} FROM {tabela}"

            if where:
                query += f" WHERE {where}"
            if order:
                query += f" ORDER BY {order}"
            if limit:
                query += f" LIMIT {limit}"

            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro na consulta: {e}")
            return []

    def update(self, tabela, dados, where, params_where=None):
        """Atualiza qualquer tabela"""
        if not self.cursor:
            return False

        try:
            set_clause = ', '.join([f"{k} = ?" for k in dados.keys()])
            valores = list(dados.values())

            if params_where:
                valores.extend(params_where)

            query = f"UPDATE {tabela} SET {set_clause} WHERE {where}"
            self.cursor.execute(query, valores)
            self.conn.commit()

            print(f"Atualizado em '{tabela}'! Linhas: {self.cursor.rowcount}")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar: {e}")
            return False

    def delete(self, tabela, where, params=None):
        """Deleta de qualquer tabela"""
        if not self.cursor:
            return False

        try:
            query = f"DELETE FROM {tabela} WHERE {where}"

            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            self.conn.commit()
            print(f"Deletado de '{tabela}'! Linhas: {self.cursor.rowcount}")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao deletar: {e}")
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Conexao fechada!")