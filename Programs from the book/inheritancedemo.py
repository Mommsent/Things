import ClassStaff

peter=ClassStaff.BasicStaff('Peter', 0)
john=ClassStaff.ManagementStaff('John', 0, 1000, 0)




print(peter)
print(john)

print('Peter\' s Pay= ', peter.calculatePay())

print('John\' s Pat= ', peter.calculatePay())
print('John\' s Performance Bonus= ', john.calculatePerBonus())
totalPay= john+peter
print('\nTotal Pay for Both Staff = ', totalPay)
