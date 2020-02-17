import pandas as pd

'''
Após encontrar a aplicação do tipo News utilize a sua
API , para identificar quais das 10 aplicações do tipo
Music e Book, possuem o maior número de citações
nessa API.
'''
class Citacao:
    def __init__(self):
        self.df = pd.read_csv("../ultis/AppleStore.csv")

    def listar_citacao(self):
        pass
