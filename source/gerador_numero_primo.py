def algo():
    	return 1 + 2

def is_prime(n):
	for i in range(3, n):
		if n % i == 0:
			return False
	return True


'''
def get_primes(input_list):
	return (e for e in input_list if is_prime(e))


def gerar_numeros():
	yield 1
	yield 2
	yield 3

for v in gerar_numeros():
	print(v, end = ' ')

nosso_gerador = gerar_numeros()
print(next(nosso_gerador))
print(next(nosso_gerador))
print(next(nosso_gerador))
'''

def get_primes(number):
	while True:
		if is_prime(number):
			yield number
		number += 1

meu_gerador = get_primes(10)
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))