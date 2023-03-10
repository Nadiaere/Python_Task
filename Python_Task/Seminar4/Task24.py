# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних.
#  Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#  Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и 
#  с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

n = int(input('Введите количество кустов на грдядке N: '))
g = list(range(1, n + 1))
g = g + g[:2]
sum = 0
for i in range(n):
    sum = max(sum, g[i] + g[i+1] + g[i-1])
print (sum)



# from math import pi, pow
# def circle(g):
#     return round(pi * pow(g, 2), 2) 

# list1 = [1, 2, 3, 4]
# max_number = max(list1)
# print("Наибольшее количество:", max_number)
  