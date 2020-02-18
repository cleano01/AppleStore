import sqlite3
from flask_restful import Resource
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

from servico.twitter import Twitter

class TwitterListener_10Tweets(StreamListener):  
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a serem coletados
        self.max_tweets = 10
        self.lista_dos_tweet = []

        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            #carrega e codifica os dados para o formato JSON
            tweet = json.loads(data)
            #Escreve o campo de data de publicação do tweet
            print("Data da publicacao do tweet")            
            print(tweet.get('created_at'))
            #Escreve o campo referente ao conteúdo do tweet
            print("Conteudo do tweet")
            print(tweet.get('text'))
            #Escreve o campo referente ao idioma do tweet
            print("Idioma do tweet")
            print(tweet.get('lang'))
            #Escreve o campo referente ao total de likes que o tweet recebeu
            print("Total de likes do tweet")
            print(tweet.get('favorite_count'))
            self.lista_dos_tweet.append(tweet)
        except BaseException as erro:
            print('Erro: ' + erro)

        #condição de parada
        if self.cont_tweet >= self.max_tweets:   
            return False

    def retorna_lista_tw(self):
        return self.lista_dos_tweet

class Citacao(Resource):

    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.servico_twitter = Twitter()
        self.apps = []


    def get(self):
        self.listar_top_app()        
        return self.coleta_app_twitter()


    def listar_top_app(self):
        try:
            resposta = self.cursor.execute('SELECT track_name FROM dados WHERE' 
            +' prime_genre = "Book" OR prime_genre = "Music"').fetchall()            
            self.apps = [i[0] for i in resposta]
        
        except Exception as e:
            return {'Erro': f'listar_citacao {e}'}


    def coleta_app_twitter(self):
        oauth = OAuthHandler(self.servico_twitter.retorna_credenciais()['consumer_key'],
        self.servico_twitter.retorna_credenciais()['consumer_secret'])
        
        oauth.set_access_token( self.servico_twitter.retorna_credenciais()['access_token'], 
        self.servico_twitter.retorna_credenciais()['access_token_secret'])
        
        tl = TwitterListener_10Tweets()
        stream = Stream(oauth, tl)
        stream.filter(track=self.apps)
        return tl.retorna_lista_tw()




        
        





