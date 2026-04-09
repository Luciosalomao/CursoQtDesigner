import sqlite3
import os


class sqlite_db:
    def __init__(self, banco=None):
        self.conn = None
        self.cursor = None

        if banco is None:
            raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            pasta_db = os.path.join(raiz_projeto, "db")
            os.makedirs(pasta_db, exist_ok=True)
            banco = os.path.join(pasta_db, "database.db")

        self.banco_nome = banco
        self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão criada com sucesso!")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao conectar: {e}")
            return False

    def criar_tabela(self, nome_tabela, campos):
        """
        Cria qualquer tabela dinamicamente

        Parâmetros:
        - nome_tabela: nome da tabela
        - campos: dicionário com campos e tipos
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
        print("Conexão fechada!")