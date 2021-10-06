'''Функция слияния словарей'''
def marger_dict(mass1,mass2):
	mass_sum=mass1.copy()
	mass_sum.update(mass2)
	print(mass_sum)

marger_dict({'Ti':47,'V':50,'Sc':44},{'Hf':178,'Ta':180,'Db':268})