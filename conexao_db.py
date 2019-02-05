import sqlite3
class Conectar():
    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo nome do banco
            print("Banco:", db_name)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False
    def commit_db(self):
        if self.conn:
            self.conn.commit()


    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")



        

    
    
