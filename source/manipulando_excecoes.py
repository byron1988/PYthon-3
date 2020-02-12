'''
def algo():
	raise Exception('excecao')
	print('depois do raise')

def algo2():
	try:
		algo()
	except:
		print('Eu peguei uma excecao')
		print('executado apos a excecao')

algo2()
'''

def divisao(divisor):

	try:
		if divisor == 13:
			raise ValueError('13 nao eh legal')
		#return 10 / divisor
	except ZeroDivisionError:
		return 'Divisao por zero'
	except TypeError:
		return 'Entre um um valor numerico'
	except ValueError:
		print('Nao utilize o numero 13')
		raise
	else:
		print('Nao ocorreu nenhuma excecao')
	finally:
		print('isso sempre sera executado')


divisao(15)

'''
try:
	raise ValueError('Este eh um argumento')
except ValueError as e:
	print('Os argumentos da exececao foram', e.args)
finally:
	print('isso sempre sera executado')
'''