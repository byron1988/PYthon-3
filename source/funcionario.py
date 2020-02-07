class Funcionario:
    
    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf

    def get_bonificacao(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, salario, cpf, senha):
        super().__init__(nome, salario, cpf)
        self.senha = senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00

gerente = Gerente("ubirani", 2500.00, "022.970.843-90", 1234)
print(gerente.__dict__, gerente.get_bonificacao())
        
