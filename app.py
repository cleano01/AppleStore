from flask import Flask, request
from flask_restful import Api

from modulos.avaliacao.Avaliacao import Avaliacao
from modulos.genero.Genero import Genero
from modulos.saida.Saida_BD import Saida_BD
from modulos.saida.Saida_CSV import Saida_CSV
from modulos.citacao.Citacao import Citacao


app = Flask(__name__)
api = Api(app)

api.add_resource(Avaliacao, '/news')
api.add_resource(Genero, '/genero')
api.add_resource(Saida_BD, '/insere/bd')
api.add_resource(Saida_CSV, '/criar/csv')
api.add_resource(Citacao, '/citacao')


if __name__ == '__main__':
    app.run(debug=True)
