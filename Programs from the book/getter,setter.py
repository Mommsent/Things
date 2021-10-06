class Point:
	WIDTH=10
	__slots__= ['__x', '__y'] # локальные дополнительные экземпляры

	def __init__(self, x = 0, y = 0): # параметры класса
		self.__x = x; self.__y = y

	def __checkValue(x): #проверка введённых данных
		if isinstance(x, int) or isinstance(x, float):
			return True
		return False

	def setCoords(self, x, y): #вывод значений класса
		if Point.__checkValue(x) and Point.__checkValue(y):
			self.__y = y
			self.__x = x
		else:
			print('Coordinate mast be numbers')

	def getCoords(self):
		return self.__x, self.__y

	def __getattribute__(self, item): # предупреждение об вызове приватной переменной
		if item=='_Point__x':
			return 'Protected attribute.'
		else:
			return object.__getattribute__(self, item)

	def __setattr__(self,key,value): # запрет изменения переменной
		if key == 'WIDTH':
			raise AttributeError
		else:
			self.__dict__[key] = value

	def __getattr__(self, item): # получение экземпляра класса
		print('__getattr__: ' + item)

	def __delattr__(self, item): # удалене экземпляра класса
		print('__delatr__: ' + item)

pt= Point(1,2)
print(pt.getCoords()) #способы вызова параметров
pt.setCoords(10,20)
print(pt.getCoords())
print(pt._Point__x)
pt.WIDTH = 5