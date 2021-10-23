population= {'Berlin': 3748148, 'Hamburg': 1822445, 'Munich': 1471508, 'Cologne': 1085664, 'Frankfurt': 753056 }
products = {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100}
grades = {'Alba': 9.5, 'Eduardo': 10, 'Normando': 3.5, 'Helena': 6.5, 'Claudia': 7.5} ### списки с которыми видем работу
student_age= dict(Amanda=27, Teresa=38, Paula=17, Mario=40) ### формировани списка через dict
products ["pillow"]=10 ### добовление элемента в список
products.update ({"shelf": 70, "sofa": 300}) ### добовление нескольких обьектов
products ["sofa"]= 400 ### изменение значения ключа
products.update ({"table": 200, "chair":20}) ### изменение нескольких значений ключа 
del population ["Cologne"] ### удаление значение по ключу
print (population) ### вывести значение на экран
student_age.pop ("Amanda")
print (student_age)