import pandas as pd
import json

class Avaliacao:
    def __init__(self):
        self.df = pd.read_csv("../ultis/AppleStore.csv")

    def maior_app_catg_news(self):
        try:
            nome_app_linha = self.df[self.df['prime_genre'] == 'News'].sort_values('rating_count_tot', ascending=False).head(1)
            track_name = nome_app_linha['track_name'].to_frame().values[0][0]
            rating_count_tot = nome_app_linha['rating_count_tot'].to_frame().values[0][0]
            size_bytes =nome_app_linha['size_bytes'].to_frame().values[0][0]
            price = nome_app_linha['price'].to_frame().values[0][0]
            prime_genre = nome_app_linha['prime_genre'].to_frame().values[0][0]

            return {'track_name':track_name, 'rating_count_tot':rating_count_tot,'size_bytes':size_bytes, 'price':price, 'prime_genre':prime_genre}
            

        except Exception as e:
            print(f'Error : listar_maior_app_catg_news {e}')  


a = Avaliacao()


print (a.maior_app_catg_news())


