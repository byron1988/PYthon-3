import math

class Forma():
    
    def __init__(self):
        print("Construtor da forma")

    def area(self):
        print("Área da forma")
    
    def perimetro(self):
        print("Perimetro da forma")

    def descricao(self):
        print("Descrição da forma")

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4

    def descricao(self):
        return "Descrição do quadrado"

class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 02

    def perimetro(self):
        return 2 * math.pi* self.raio

    def descricao(self):
        return "Descrição do círculo"
    


quadrado = Quadrado(2)
print(quadrado.area())
print(quadrado.perimetro())
print(quadrado.descricao())

circulo = Circulo(2)
print(circulo.area())
print(circulo.perimetro())
print(circulo.descricao())