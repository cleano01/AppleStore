import pandas as pd

class Genero:
    def __init__(self):
        self.df = pd.read_csv("../ultis/AppleStore.csv")
        self.lista_top_book =[] 
        self.lista_top_music = []

    def top10_app_catg_book(self):
        try:
            lista_app_linha = self.df[self.df['prime_genre'] == 'Book']\
            .sort_values('rating_count_tot', ascending=False).head(10)
            
            track_name = lista_app_linha['track_name'].to_frame().values
            rating_count_tot = lista_app_linha['rating_count_tot'].to_frame().values[0][0]
            size_bytes = lista_app_linha['size_bytes'].to_frame().values
            price = lista_app_linha['price'].to_frame().values
            prime_genre = lista_app_linha['prime_genre'].to_frame().values

            for t, r, s, p, pg in zip(track_name, rating_count_tot, size_bytes, price, prime_genre ):
                self.lista_top_book.append((t[0], r[0], s[0], p[0], pg[0]))

            #track_name, n_citacoes, size_bytes, price, prime_genre.
            return self.lista_top_book

        except Exception as e:
            print(f'Error : top10_app_catg_Book {e}')
        

    def top10_app_catg_music(self):
        try:
            lista_app_linha = self.df[self.df['prime_genre'] == 'Music']\
            .sort_values('rating_count_tot', ascending=False).head(10)
            
            track_name = lista_app_linha['track_name'].to_frame().values
            rating_count_tot = lista_app_linha['rating_count_tot'].to_frame().values[0][0]
            size_bytes = lista_app_linha['size_bytes'].to_frame().values
            price = lista_app_linha['price'].to_frame().values
            prime_genre = lista_app_linha['prime_genre'].to_frame().values

            for t, s, p, pg in zip(track_name, rating_count_tot,size_bytes, price, prime_genre):
                self.lista_top_music.append((t[0], s[0], p[0], pg[0]))

            return self.lista_top_music
        
        except Exception as e:
            print(f'Error : top10_app_catg_Music {e}')
        

a = Genero()
print (a.top10_app_catg_book())
        
print("###")

print(a.top10_app_catg_music())

