import csv
import sqlite3
from flask_restful import Resource


class Saida_CSV(Resource):

    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()

    def get(self):
        self.retorna_csv()
    
    def retorna_csv(self):
        resposta = self.cursor.execute('SELECT * FROM dados')

        for row in resposta:
            print(row[1])

        return 'ok'
    

