import pandas as pd

class Genero:
    def __init__(self):
        self.df = pd.read_csv("../../ultis/AppleStore.csv")
       
    def top10_app_catg_book(self):
        try:
            lista_app_linha = self.df[self.df['prime_genre'] == 'Book'].sort_values('rating_count_tot', ascending=False).head(10)
            return lista_app_linha['track_name'].to_frame().values
        except:
            print('Error : top10_app_catg_Book')
        

    def top10_app_catg_music(self):
        try:
            lista_app_linha = self.df[self.df['prime_genre'] == 'Music'].sort_values('rating_count_tot', ascending=False).head(10)
            return lista_app_linha['track_name'].to_frame().values
        except:
            print('Error : top10_app_catg_Music')
        


        

