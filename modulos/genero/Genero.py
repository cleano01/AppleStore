import pandas as pd
from flask_restful import Resource

class Genero(Resource):
    def __init__(self):
        self.df = pd.read_csv("ultis/AppleStore.csv")
        self.lista_top=[] 


    def get(self):
        try:
            self.top10_app_catg_book()
            self.top10_app_catg_music()
            return self.lista_top

        except Exception as e:
            return {'Error' : f'Não possilvél retornar a lista dos tops 10 {e}'}
            

    def top10_app_catg_book(self):
        try:
            lista_app_linha = self.df[self.df['prime_genre'] == 'Book']\
            .sort_values('rating_count_tot', ascending=False).head(10)
            
            track_name = lista_app_linha['track_name'].to_frame().values
            rating_count_tot = lista_app_linha['rating_count_tot'].to_frame().values
            size_bytes = lista_app_linha['size_bytes'].to_frame().values
            price = lista_app_linha['price'].to_frame().values
            prime_genre = lista_app_linha['prime_genre'].to_frame().values

            for t, r, s, p, pg in zip(track_name, rating_count_tot ,size_bytes, 
            price, prime_genre ):
                self.lista_top.append((t[0], float(r[0]) , float(s[0]), 
                p[0], pg[0]))

            return self.lista_top

        except Exception as e:
            print(f'Error : Error na função top10_app_catg_Book {e}')
        

    def top10_app_catg_music(self):

        try:
            lista_app_linha = self.df[self.df['prime_genre'] == 'Music']\
            .sort_values('rating_count_tot', ascending=False).head(10)
            
            track_name = lista_app_linha['track_name'].to_frame().values
            rating_count_tot =  lista_app_linha['rating_count_tot'].to_frame().values
            size_bytes = lista_app_linha['size_bytes'].to_frame().values
            price = lista_app_linha['price'].to_frame().values
            prime_genre = lista_app_linha['prime_genre'].to_frame().values
            
            for t, r, s, p, pg in zip(track_name, rating_count_tot, size_bytes, 
            price, prime_genre):
                self.lista_top.append((t[0], float(r[0]), float(s[0]), 
                p[0], pg[0]))

            return self.lista_top
        
        except Exception as e:
            print(f'Error : Erro na função top10_app_catg_Music {e}')
        





