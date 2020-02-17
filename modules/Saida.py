import sqlite3
from  Avaliacao import Avaliacao

class Saida:
    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.avaliacoes = Avaliacao()

    def insere_ctg_new(self):
        self.criar_tabela()

        track_name = self.avaliacoes.maior_app_catg_news()['track_name']
        size_bytes = self.avaliacoes.maior_app_catg_news()['size_bytes']
        price = self.avaliacoes.maior_app_catg_news()['price']
        prime_genre = self.avaliacoes.maior_app_catg_news()['prime_genre']
        n_citacoes=0

        self.inserir_dados_ctg_new(track_name, n_citacoes, 
        int(size_bytes), price, prime_genre)
    
    def criar_tabela(self):
       
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dados (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            track_name TEXT NOT NULL,
            n_citacoes  REAL DEFAULT 0,
            size_bytes  REAL NOT NULL,
            price  REAL NOT NULL,
            prime_genre TEXT NOT NULL
            );
        """)

        print('Tabela criada com sucesso.')

    #track_name, n_citacoes, size_bytes, price, prime_genre
    
    def inserir_dados_ctg_new(self,*args):
        lista=[args]
        print('####')
        self.cursor.executemany('INSERT INTO dados (track_name, n_citacoes, size_bytes, price, prime_genre)VALUES (?, ?, ?, ?, ?)', lista)
        self.conn.commit()
        # desconectando...
        self.conn.close()
        print('Dados salvos com sucesso')
    
    
    
s = Saida()

s.insere_ctg_new()