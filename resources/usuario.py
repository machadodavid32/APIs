from flask_restful import Resource, reqparse
from models.usuario import UserModel


class User(Resource):  # Aqui estou fazendo o primeiro recurso da api
    
    def get(self, user_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()        
        return {'message': 'Hotel not found'}, 404   # Aqui caso ele não encontre o hotel, vai retornar esta mensagem.    
    
    
    
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel'}, 500    
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found'}, 404
    