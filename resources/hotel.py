from flask_restful import Resource, reqparse
from models.hotel import HotelModel


hoteis = [
    
    {'hotel_id': 'alpha',
     'nome': 'Alpha Hotel',
     'estrelas': 4.3,
     'diaria': 420.34,
     'cidade': 'Rio de Janeiro'},
    
    {'hotel_id': 'bravo',
     'nome': 'Bravo Hotel',
     'estrelas': 4.4,
     'diaria': 380.90,
     'cidade': 'Blumenau'},
    
    {'hotel_id': 'charlie',
     'nome': 'Charlie Hotel',
     'estrelas': 3.9,
     'diaria': 320.20,
     'cidade': 'São Paulo'}
]


class Hoteis(Resource):  # Aqui estou fazendo o primeiro recurso da api
    def get(self):
        return {'hoteis': hoteis}



class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    

    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel        
        return {'message': 'Hotel not found'}, 404   # Aqui caso ele não encontre o hotel, vai retornar esta mensagem.    
    
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):  # evitar que se crie um hotel ja cadastrado.
            return {"message": "Hotel id '{}' already existis.".format(hotel_id)}, 400
        
        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)  # Aqui precisa pegar todos os objetos do HotelModel e para não colocar todos...
        #...fazemos **dados para completar em vez de ficar escrevendo um por um.
        hotel.save_hotel()
        return hotel.json()
         
    
    def put(self, hotel_id):
       
       dados = Hotel.argumentos.parse_args()
       hotel_objeto = HotelModel(hotel_id, **dados)
       novo_hotel = hotel_objeto.json()
       hotel = Hotel.find_hotel(hotel_id)
       if hotel:
           hotel.update(novo_hotel)
           return novo_hotel, 200
       hoteis.append(novo_hotel)
       return novo_hotel, 201 # created - criado com sucesso    
           
        
        
    
    def delete(self, hotel_id):
        global hoteis
        hoteis = [ hotel for hotel in hoteis if hotel ['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}
    