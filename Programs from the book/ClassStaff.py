class Staff:

	def __init__(self, pPosition, pName,pPay):
		self._position=pPosition
		self.name=pName
		self.pay=pPay
		print('Creating Staff object')

	def __srt__(self):
		return "Position = %s, Name=%s, Pay=%d" %(self._position, self.name, self.pay)

	def calculatePay(self):
		prompt = '\nEnter number of hpurs worked for' \
				 '%s: ' %(self.name)
		hours=input(prompt)
		prompt='Enter the hourly rate for %s: ' %(self.name)
		hourlyRate= input(prompt)
		self.pay= int(hours)*int(hourlyRate)
		return self.pay

	@property
	def position(self):
		print("Getter Method")
		return self._position

	@position.setter
	def position(self, value):
		if value== 'Manager' or value== 'Basic':
			self._position=value
		else:
			print('Position is invalid. No changes made.')

class ManagementStaff(Staff):
	def __init__(self, pName, pPay, pAllowance, pBonus):
		super().__init__('Manager', pName, pPay)
		self.allowance=pAllowance
		self.bonus=pBonus

	def calculatePay(self):
		basicPay=super().claculatePay()
		self.pay=basicPay+self.allowance
		return self.pay

	def calculatePerBonus(self):
		prompt='Enter performance grade for %s: %(self.name)'
		grade=input(prompt)
		if (grade == 'A'):
			self.bonus=1000
		else:
			self.bonus=0
		return self.bonus

	def __add__(self, other):
		return self.pay + other.pay

class BasicStaff(Staff):
	def __init__(self,pName,pPay):
		super().__init__('Basic', pName, pPay)


officesStaff1=Staff('Basic', 'Yvonne', 0)
officesStaff1 = Staff('Basic', 'Yvonne', 0)
print(officesStaff1.position)

class A:
	def __init__(self):
		self.__x=5
		self._y=6
varA=A()
print(varA._y)