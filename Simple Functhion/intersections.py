'''Функция выявления пересечений списков'''
def lists(first_list, second_list):
	crossing_list=[]
	for number in first_list:
		for another_namber in second_list:
			if number == another_namber:
				crossing_list.append(another_namber)
	print(crossing_list)

