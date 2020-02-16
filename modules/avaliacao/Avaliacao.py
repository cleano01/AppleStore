import pandas as pd

class Avaliacao:
    def __init__(self):
        self.df = pd.read_csv("../../ultis/AppleStore.csv")

    def listar_maior_valor(self):

        '''valor_maximo = self.df[self.df['prime_genre'] == 'News']['rating_count_tot'].max()
        nome_app_linha = self.df.loc[(self.df['rating_count_tot'] == valor_maximo)]
        captura_nome_app= nome_app_linha['track_name'].to_frame().values
       
        print(valor_maximo)
        #return captura_nome_app[0][0]
        '''
        
        nome_app_linha = self.df[self.df['prime_genre'] == 'News'].sort_values('rating_count_tot', ascending=False).head(1)
        
        return nome_app_linha['track_name'].to_frame().values[0][0]





a = Avaliacao()
x =a.listar_maior_valor()
print(x)    