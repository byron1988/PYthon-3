
class Operador():

	def __init__(self, numero):
		self.numero = numero

	def __add__(self, op):
		return self.numero ** op.numero

	def __mul__(self, op):
		return self.numero / op.numero

	def __sub__(self, op):
		return self.numero * op.numero

if __name__ == '__main__':
	x = Operador(10)
	y = Operador(2)
	print(x + y)
	print(x*y)
	print(x - y)