from flask import Flask, request
from flask_restful import Api

from modulos.avaliacao.Avaliacao import Avaliacao
from modulos.genero.Genero import Genero
from modulos.saida.Saida_BD import Saida_BD
from modulos.saida.Saida_CSV import Saida_CSV
from modulos.citacao.Citacao import Citacao


app = Flask(__name__)
api = Api(app)

# retorna o app com maior avaliações com a categoria news
api.add_resource(Avaliacao, '/news')
#retorna os 10 maior app com as categorias book e music
api.add_resource(Genero, '/genero')
#insere dados no banco de dados das rotas genero e news
api.add_resource(Saida_BD, '/insere/bd')
#retorna um csv com todos os dados do banco de ados
api.add_resource(Saida_CSV, '/criar/csv')
#retorna um as citacoes de genereo book e news do twitter
api.add_resource(Citacao, '/citacao')


if __name__ == '__main__':
    app.run(debug=True)
