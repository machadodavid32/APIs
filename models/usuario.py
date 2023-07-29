from sql_alchemy import banco
# importação do banco do arquivo para realizar o sqlalchemy

class UserModel(banco.Model):
    
    __tablename__ = 'usuarios'  # nome da tabela no sqlalchemy
    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))
    # Com esses dados (linhas 5 até 10) nós mapeamos os dados para que o sql alchmey o reconheça como um banco de dados.
    
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def json(self):
        """Função que vai converter o objeto em um formato json"""
        return{
            'user_id': self.user_id,
            'login': self.login
        }    
    
    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()  # SELECT * FROM hoteis WHERE hotel_id = hotel_id
        if user:
            return user  # Se existe hotel, retorne hotel
        return None # Se não existe, retorne None
    
    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first() 
        if user:
            return user
        return None
    
        
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()
            
    

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
                    