# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted(students)
grades[0] = sum(grades[0])/len(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])
my_dict = {'Aaron': grades[0], 'Bilbo': grades[1], 'Johnny': grades[2], 'Khendrik': grades[3], 'Steve': grades[4]}
print(my_dict)
