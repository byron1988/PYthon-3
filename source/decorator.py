'''
Decorator - é uma função que recebe outra função como parâmetro, gera uma nova função que adiciona algumas funcionalidades à função original e a retorna essa nova função.
'''

'''
def modificar(funcao):
	def subtrair(a, b):
		return a - b
	return subtrair

@modificar	
def somar(a, b):
	return a + b

print(somar(2, 3))
'''

'''
def modificar(funcao):
	def somar_pares(a, b):
		if a % 2 == 0 or b % 2 == 0:
			return a + b
		return a - b
	return somar_pares

@modificar	
def somar(a, b):
	return a + b

print(somar(11, 1))
'''

def meu_decorador(funcao):
	def imprime_algo():
		print('eu nao sei somar')
	return imprime_algo

@meu_decorador
def imprime():
	print('eu sei somar')

#imprime = meu_decorador(imprime)
imprime()