import pandas as pd

class Avaliacao:
    def __init__(self):
        self.df = pd.read_csv("../../ultis/AppleStore.csv")

    def maior_app_catg_news(self):
        try:
            nome_app_linha = self.df[self.df['prime_genre'] == 'News'].sort_values('rating_count_tot', ascending=False).head(1)
            return nome_app_linha['track_name'].to_frame().values[0][0]
        except:
            print('Error : listar_maior_app_catg_news')
       





