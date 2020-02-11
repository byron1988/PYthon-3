class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, CPF):
        super().__init__(nome, idade)
        self.CPF = CPF

class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, CJPJ):
        super().__init__(nome, idade)
        self.CNPJ = CJPJ

pessoa = Pessoa("ubirani", 28)
pessoa_fisica = PessoaFisica("ubirani", 28, "022.970.843-90")
pessoa_juridica = PessoaFisica("ubirani", 28, "83.101.053/0001-26")

print(pessoa.__dict__)
print(pessoa_fisica.__dict__)
print(pessoa_juridica.__dict__)