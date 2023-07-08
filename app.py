from flask import Flask
from flask_restful import Resource, Api

""" Vamos desenvolver uma api para pesquisar por hoteis, saber localização e preços."""

app = Flask(__name__)
api = Api(app)

class Hoteis(Resource):  # Aqui estou fazendo o primeiro recurso da api
    def get(self):
        return {'hoteis': 'meus hoteis'}
    
api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':  # Aqui é uma configuração padrão do flask
    app.run(debug=True)  # Modo debug=True enquanto está em desenvolvimento, após isso ou retirar ou colocar como False
        

# Running on http://127.0.0.1:5000/hoteis    Aqui é a raiz do site. Se tudo


# INSTRUÇÕES
# Após fazer os passos acima, abrir o programa postman:
# Abrir uma nova collection
# add um requisição e coloque um nome. No campo GET adicione o endereço acima