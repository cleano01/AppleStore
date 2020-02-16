import pandas as pd
'''Identificar quais são as 10 Aplicações do gênero Music
e Book que possuem a maior quantidade de
avaliações no arquivo csv apple_store.'''
class Genero:
    def __init__(self):
        self.df = pd.read_csv("../../ultis/AppleStore.csv")
        self.top_10_music = []
        self.top_10_book = []

    def top10_app_catg_Book(self):
        lista_app_linha = self.df[self.df['prime_genre'] == 'Book'].sort_values('rating_count_tot', ascending=False).head(10)
        #lista_app_linha['track_name']
        print(lista_app_linha['track_name'].to_frame().values)

    def top10_app_catg_Music(self):
        lista_app_linha = self.df[self.df['prime_genre'] == 'Music'].sort_values('rating_count_tot', ascending=False).head(10)
        
        print(lista_app_linha)

        

g = Genero()
g.top10_app_catg_Book()