class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome':self.nome, 'salario':self.salario}    
    

David = Funcionario("David", 7000)

print(David.dados())


class Admin(Funcionario):    # aqui é a herança(Funcionário)
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados        
    

fernando = Admin('Fernando', 14000)    

print(David.dados())
print(fernando.dados())

print(fernando.atualizar_dados(2100))



