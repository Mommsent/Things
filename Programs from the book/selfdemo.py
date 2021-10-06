class ProgStaff:
	companyName='ProgramingLab'

	def __init__(self, pSalary):
		self.salary=pSalary

	def printInfo(self):
		print('Company name is', ProgStaff.companyName)
		print('Salary is', self.salary)
peter=ProgStaff(2500)
john=ProgStaff(2500)

ProgStaff.companyName='ProgrammingShool'
peter.salary=2700
print(peter.companyName)
print(john.companyName)
print(peter.salary)
print(john.salary)
john.printInfo()
ProgStaff.printInfo(john)


