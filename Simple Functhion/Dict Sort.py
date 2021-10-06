'''Функция ввода и сортировки списка покупок'''
def sort_dictionary():
	dictionary =dict()
	while True: #цикл заполнения словаря через введение вручную данных
		key=str(input('Введите товар: '))
		if key=='':
			break
		value=int(input('Введите количество товара: '))
		dictionary[key]=value
	print('Введите "1" если хотите отсортировать словарь в порядке возростания и "2" если в порядке убывания.')
	user_input=int(input()) #сортировка словаря в порядке возрастания или убывания, на усмотрение пользователя
	if user_input==1:
		for increase_values in sorted(dictionary.values()):
			print(increase_values)
	elif user_input==2:
		for waning_values in sorted(dictionary.values(), reverse=True):
			print(waning_values)
	else:
		print('Вы ввели не выерный символ, пожалуйста, укажите "1" или "2" в качестве указателя')
	print('Товары отсортированы.')

sort_dictionary()