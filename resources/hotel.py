from flask_restful import Resource, reqparse


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
    
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel            
        return None  
    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel        
        return {'message': 'Hotel not found'}, 404   # Aqui caso ele não encontre o hotel, vai retornar esta mensagem.    
    
    
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        
        novo_hotel = {'hotel_id': hotel_id, **dados }
        
        hoteis.append(novo_hotel)
        return novo_hotel, 200  # 200 código de sucesso, que deu certo.
    
    
    def put(self, hotel_id):
       
       dados = Hotel.argumentos.parse_args()
       novo_hotel = {'hotel_id': hotel_id, **dados }  # conceito de kwargs, que vai desempacotar os dados sem precisar colocar...
           #...todas as chaves e valores, reduzindo muito a linha de código.
       
       hotel = Hotel.find_hotel(hotel_id)
       if hotel:
           hotel.update(novo_hotel)
           return novo_hotel, 200
       hoteis.append(novo_hotel)
       return novo_hotel, 201 # created - criado com sucesso    
           
       
       
        
    
    def delete(self, hotel_id):
        pass