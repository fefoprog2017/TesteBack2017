from conexao_db import*

#Classe principal.
class tb_customer(object):
    tb_name = 'tb_customer_account'
    def __init__(self):
        self.db = Conectar('teste.db')
        self.tb_name    
    def close_connection(self):
        self.db.close_db()
        
    #Função para criar a tabela.
    def criar_schema(self, schema_name='customer_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)
        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False
        print("Tabela %s criada com sucesso." % self.tb_name)
        
    #Função criada para inserir dados por uma lista.
    def inserir_lista(self):
        lista = [('1000','12345678945','Ruan',1,'400'),('2125','12345458988','Jorge',1,'740'),('262','77788899487','Jairo',1,'180')]
        try:
            self.db.cursor.executemany("""INSERT INTO tb_customer_account (id_customer, cpf_cnpj, nm_customer, is_active, vl_total) VALUES (?,?,?,?,?)""",lista)
            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos da lista com sucesso: %s registros." %len(lista))
        except sqlite3.IntegrityError:
            return False
        
    #Função criada para selecionar todos os dados da tabela.
    def meu_select(self, sql="SELECT * FROM tb_customer_account;"):
        r = self.db.cursor.execute(sql)
        # gravando no bd
        self.db.commit_db()
        for tabela in r.fetchall():
            print(tabela)
    #Função criada para selecionar a Média.
    def meu_select_media(self, sql="SELECT AVG(vl_total)FROM tb_customer_account WHERE vl_total > '560' and id_customer between '1500' and '2700';"):
        r = self.db.cursor.execute(sql)
        # gravando no bd
        self.db.commit_db()
        print("Calculando Média... ")
        for tabela in r.fetchall():
            print("Média: %s " % tabela)

    #Função criada para selecionar a Média.
    def meu_select_media_order(self, sql="select * from tb_customer_account where  vl_total > '560' and  id_customer between 1500 and 2700 order by vl_total desc;"):
        r = self.db.cursor.execute(sql)
        # gravando no bd
        self.db.commit_db()
        print("\/ Usamos Estes clientes para calcular a média \/. ")
        for tabela in r.fetchall():
            print(tabela)


            
        
#main.
if __name__ == '__main__':
    c = tb_customer()
    c.criar_schema()
    c.inserir_lista()
    c.meu_select_media()
    c.meu_select_media_order()

