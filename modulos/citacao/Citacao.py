import pandas as pd
import sqlite3
from flask_restful import Resource

'''
Após encontrar a aplicação do tipo News utilize a sua
API , para identificar quais das 10 aplicações do tipo
Music e Book, possuem o maior número de citações
nessa API.
'''
class Citacao(Resource):
    def __init__(self):
        #self.df = pd.read_csv("../ultis/AppleStore.csv")
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()

    def get(self):
        return self.listar_citacao()

    def listar_citacao(self):
        try:
            resposta = self.cursor.execute('SELECT track_name ,max(prime_genre) FROM dados WHERE' 
            +' prime_genre = "Book" OR prime_genre = "Music"').fetchall()[0]
        
            return {'app':resposta[0], 'genero':resposta[1]}
        
        except Exception as e:
            return {'Erro': f'listar_citacao {e}'}
        





