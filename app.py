from flask import Flask, request
from flask_restful import Api

from modulos.avaliacao.Avaliacao import Avaliacao
from modulos.genero.Genero import Genero
from modulos.saida.Saida import Saida

app = Flask(__name__)
api = Api(app)

api.add_resource(Avaliacao, '/news')
api.add_resource(Genero, '/genero')
api.add_resource(Saida, '/insere')

if __name__ == '__main__':
    app.run(debug=True)
