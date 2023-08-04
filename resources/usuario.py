from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token
from secrets import compare_digest
from flask_jwt_extended import jwt_required, get_jwt
from blacklist import BLACKLIST


atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")

class User(Resource):  # Aqui estou fazendo o primeiro recurso da api
    #/usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()        
        return {'message': 'User not found'}, 404   # Aqui caso ele não encontre o hotel, vai retornar esta mensagem.    
    
    
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found'}, 404
    
    
class UserRegister(Resource):
    #/cadastrado
    def post(self):
    
        dados = atributos.parse_args()   
        
        if UserModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exists.".format(dados['login'])}
        
        user = UserModel(**dados)
        user.save_user()
        return {"message" : "User created succesfully!"}, 201 # created
    
class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        
        user = UserModel.find_by_login(dados['login'])    
        
        if user and compare_digest(user.senha, dados['senha']): # importado de secrets
            token_de_acesso = create_access_token(identity=user.user_id) # create_access_token importado do flask jtw - criação de um token de acesso.
            return {'access_token': token_de_acesso}, 200
        return {'message': 'The username or password is incorrect'}, 401
    
    # aqui instalamos outra biblioteca: pip install Flask-JWT-Extended
    

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']  # jti = jtw + Token + Identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out succesfully!'}, 200
        