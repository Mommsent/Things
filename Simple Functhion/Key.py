spam={'color':'red', 'age':42}
for v in spam.values():
	print(v)

for k,v in spam.items():
	print('Key: '+ k + ' Value: '+str(v))

print('name' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)

picnicItems={'apples':5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0))+ ' cups')
print('I am bringing ' + str(picnicItems.get('eggs', 0))+ ' eggs')