import heapq

class FilaDePrioridade:

	def __init__(self):
		self.fila = []
		self.indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self.fila, (-prioridade, self.indice, item))
		self.indice += 1

	def remover(self):
		return heapq.heappop(self.fila)[-1]


class Item:

	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome


fila = FilaDePrioridade()
fila.inserir(Item('Cristhiany'), 25)
fila.inserir(Item('Ubirani'), 31)
fila.inserir(Item('Sandra'), 60)

print(fila.remover())
print(fila.remover())
print(fila.remover())