import csv
import sqlite3
from flask_restful import Resource


class Saida_CSV(Resource):

    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()

    def get(self):
        try:
            self.retorna_csv()
            return{'Status': 'Gravação feita com sucesso'}

        except Exception as e:
            return {'Error': f'Não foi possivel fazer a gração {e}'}

    def retorna_csv(self):
        try:
            resposta = self.cursor.execute('SELECT * FROM dados')        
            arquivo = open('AppleStore.csv', 'w')
            escrever = csv.writer(arquivo)
            
            #titulo do meu csv
            escrever.writerow(('id','track_name', 'n_citacoes', 'size_bytes', 
            'price', 'prime_genre'))

            for row in resposta:
                escrever.writerow( (row[0], row[1], row[2], row[3], 
                row[4],row[5]))
            arquivo.close()
            return {'Status': 'Gravação feita com sucesso'}

        except Exception as e:
            return {'Error': f'retorna_csv {e}'}
        
    

