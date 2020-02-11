# parte 1 abstract class
from abc import ABCMeta, abstractmethod

class MinhaClasseAbstrata(metaclass=ABCMeta):

	@abstractmethod
	def fazer_algo(self):
		pass

	@abstractmethod
	def fazer_algo_novamente(self, o_que_fazer):
		pass
# não pode ser instaciada diretamente
# obj = MinhaClasseAbstrata()

# parte 2 abstract class

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

	@abstractmethod
	def dizer_algo(self):
		return 'Eu sou um animal'


class Cachorro(Animal):
	
	def dizer_algo(self):
		s = super(Cachorro, self).dizer_algo()
		return '%s - %s' % (s, 'AU AU')
	

c = Cachorro()
print(c.dizer_algo())