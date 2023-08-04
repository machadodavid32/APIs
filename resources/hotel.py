from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required    





class Hoteis(Resource):  # Aqui estou fazendo o primeiro recurso da api
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}



class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome'cannot be left blank")
    atributos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank")
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')
    

    
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()        
        return {'message': 'Hotel not found'}, 404   # Aqui caso ele não encontre o hotel, vai retornar esta mensagem.    
    
    @jwt_required()  # Aqui significa que a pessoa tem que estar logada para postar alguma alteração
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):  # evitar que se crie um hotel ja cadastrado.
            return {"message": "Hotel id '{}' already existis.".format(hotel_id)}, 400
        
        
        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(hotel_id, **dados)  # Aqui precisa pegar todos os objetos do HotelModel e para não colocar todos...
        #...fazemos **dados para completar em vez de ficar escrevendo um por um.
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 #internal server error    
        return hotel.json()
         
    @jwt_required()
    def put(self, hotel_id):
       
       dados = Hotel.atributos.parse_args()      
       hotel_encontrado = HotelModel.find_hotel(hotel_id)
       if hotel_encontrado:
           hotel_encontrado.update_hotel(**dados)
           hotel_encontrado.save_hotel()
           return hotel_encontrado.json(), 200
       hotel = HotelModel(hotel_id, **dados)
       try:
           hotel.save_hotel()
       except:
           return {'message': 'An internal error ocurred trying to save hotel.'}, 500 #internal server error
       
       return hotel.json(), 201 # created - criado com sucesso    
           
        
        
    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel'}, 500    
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found'}, 404
    