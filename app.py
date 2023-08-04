from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager  # serve para gerenciar toda a parte de autenticação
from blacklist import BLACKLIST

""" Vamos desenvolver uma api para pesquisar por hoteis, saber localização e preços."""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #Aqui define o caminho e o nome do nosso banco no slqalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para evitar avisos que atrasam a
app.config['JWT_SECRET_KEY'] = 'dontTellAnyone' #Configuração necessária para uma garantir a criptografia
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request  # ou seja, antes da primeira requisição.
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out'}), 401  # converte um dicionário para json        
        
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


if __name__ == '__main__':  # Aqui é uma configuração padrão do flask
    from sql_alchemy import banco
    banco.init_app(app)  # Para ser executado somente no arquivo principal(main = app.py)
    app.run(debug=True)  # Modo debug=True enquanto está em desenvolvimento, após isso ou retirar ou colocar como False
        
# Abrir anbiente virtual david_api/Scripts/Activate
# No terminal, digitar python app.py + enter
# Running on http://127.0.0.1:5000/hoteis    Aqui é a raiz do site. Se tudo


# INSTRUÇÕES
# Após fazer os passos acima, abrir o programa postman:
# Abrir uma nova collection
# add um requisição e coloque um nome. No campo GET adicione o endereço acima

# Após a criação, no lado esquerdo do programa postman, clique em /hoteis e clique em duplicar.
# Ao duplicar, rename para /hoteis/{hotel_id}
# duplique novamente,mude o de 'get' para 'post' e clique em salvar
# duplique, mude para 'put' e clique em salvar
# duplique, mude para 'del' e clieque em salvar.

# Após os passos acima, voltamos ao código(linha 12) e criamos um novo endpoint que acabamos de criar no postman com os passos acima


# Agora vamos a criação do post, indo em postman, clincando no post abaixo do get, depois clicar em body,..
# raw, selecionar json, e colar o codigo json que contenha as chaves hotel_id, nome, estrelas, etcc.
# retire o id e deixe somente nome, estrelas, cidade, diaria - e clique em salvar.
# No arquivo hotel.py, importe a biblioteca reaparse - que vai servir para requisição. Na classe post, faça a configuração.


# Para criação do put, mesmo esquema do post no postman. Depois vamos ao codigo no hotel.py
# Obs: No caso do put, se o hotel não existir, ele vai criar quando digitarmos os dados, no caso se ele existir, ele vai atualizar..
# .. ou subscrever


# Após a implementação DOS TOKENS, para adicionar um hotel ou um usuario, vá no campo 'post' em postman....
# coloque os dados do novo hotel, vá no cabeçalho 'header' e digite Authorization no campo 'key' ...
# e digite no campo ao lado(Value) a palavra 'Bearer'