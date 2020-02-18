import sqlite3
from flask_restful import Resource

from modulos.avaliacao.Avaliacao import Avaliacao
from modulos.genero.Genero import Genero

class Saida (Resource):

    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.avaliacoes = Avaliacao()
        self.generos = Genero()
    
    def get(self):
        
        try:
            self.criar_tabela()
            self.insere_ctg_new()
            self.insere_top_10()
            return {'status':'sucesso' }
        
        except Exception as e:
            return {'Error': 'error ao inserir dados no BD'}
       


    def insere_ctg_new(self):
        
        try:
            track_name = self.avaliacoes.get()['track_name']
            n_citacoes= self.avaliacoes.get()['rating_count_tot']
            size_bytes = self.avaliacoes.get()['size_bytes']
            price = self.avaliacoes.get()['price']
            prime_genre = self.avaliacoes.get()['prime_genre']
            
            self.inserir_dados_bd(track_name, n_citacoes, 
            size_bytes, price, prime_genre)

        except Exception as e:
            print(f'Error : insere_ctg_new {e}')


    def insere_top_10(self):
        
        for i in self.generos.get():
            self.inserir_dados_bd(i[0], i[1], 
            i[2], i[3], i[4])
    
            
    def criar_tabela(self):
        
        try:
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

        except Exception as e:
            print(f'Erro : criar_tabela {e}')
       
         
    def inserir_dados_bd(self,*args):
        
        try:   
            curso = self.conn.cursor()
         
            lista=[args]
            curso.executemany('INSERT INTO dados \
            (track_name, n_citacoes, size_bytes, price, prime_genre)\
            VALUES (?, ?, ?, ?, ?)', lista)

            self.conn.commit()

            # desconectando...
            curso.close()
            print('Dados salvos com sucesso')
        
        except Exception as e:
            print(f'Erro :  inserir_dados_ctg_new {e}')
            
       
    
    
    
