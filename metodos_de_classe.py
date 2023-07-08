class Funcionario():
    aumento = 1.04
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome':self.nome, 'salario':self.salario}    
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aplicar_aumento
        
    @classmethod
    def definir_novo_aumento(cls, novo_aumento):  # Aqui em vez de pegar o proprio atributo da função, ele pega o atributo da classe.
        cls.aumento = novo_aumento
    
    @staticmethod  # Aqui não exige nenhum método da classe
    def dia_util(dia):  
        if dia.weekday() == 5 or dia.weekday() == 6:  # Segundo o comando weekday, 0=domingo e 6=sabado, 1=segund, 2=terça....e por ai vai
            return False
        return True    

 


        
Funcionario.definir_novo_aumento(1.05)
David = Funcionario("David", 7000)

pedro = Funcionario("pedro", 8000)
pedro.aplicar_aumento()
pedro.dados()


