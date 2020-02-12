class Pessoa:

    def __init__(self, nome):
        self.nome  = nome
    
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)

p = Pessoa("Ubirani")
print(p.nome)

p2 = Pessoa.outro_construtor("ubirani 2")
print(p2.nome)