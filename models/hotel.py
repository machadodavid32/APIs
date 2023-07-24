from sql_alchemy import banco
# importação do banco do arquivo para realizar o sqlalchemy

class HotelModel(banco.Model):
    
    __tablename__ = 'hoteis'  # nome da tabela no sqlalchemy
    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))  # aqui uma casa depois da virgula
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))
    # Com esses dados (linhas 5 até 10) nós mapeamos os dados para que o sql alchmey o reconheça como um banco de dados.
    
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    
    def json(self):
        """Função que vai converter o objeto em um formato json"""
        return{
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }    
    
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()  # SELECT * FROM hoteis WHERE hotel_id = hotel_id
        if hotel:
            return hotel  # Se existe hotel, retorne hotel
        return None # Se não existe, retorne None
    
        
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()
            