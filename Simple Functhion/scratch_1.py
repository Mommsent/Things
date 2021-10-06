spam={'color':'red', 'age':42}
for v in spam.values():
	print(v)

for k,v in spam.items():
	print('Key: '+ k + ' Value: '+str(v))

print('name' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)