
'''class P():

    def __init__(self,x):
        self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

p = P(10)        
print(p.getX())
p.setX(3)
print(p.getX())'''

"""
Encapsulamento é tratado com @property
"""
class P():
	
	def __init__(self, x):
		self.x = x

	@property
	def x(self):
		return self._x
	
	@x.setter
	def x(self, x):
		if x > 0:
			self._x = x

p = P(10)
print(p.x)
p.x = -3
print(p.x)