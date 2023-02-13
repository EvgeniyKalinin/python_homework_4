# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите колличество элементов первого массива  -->   "))
m = int(input("Введите колличество элементов второго массива  -->   "))
list_1 = []
list_2 = []


for i in range(n):
    num_1 = int(input(f"Введите [{i}] элемент ПЕРВОГО массива -->   "))
    list_1.append(num_1)
print()


for i in range(m):
    num_2 = int(input(f"Введите [{i}] элемент ВТОРОГО массива -->   "))
    list_2.append(num_2)
print()


if len(list_1) < len(list_2):
    short_list = list_1
    long_list = list_2
else:
    short_list = list_2
    long_list = list_1


final_list = []
for i in range(len(short_list)):
    for j in range(len(long_list)):
        if long_list[j] == short_list[i]: 
             final_list.append(short_list[i])


final_numbers = set(final_list)
final_list = list(final_numbers)
list.sort(final_list)


print(f"{n} {m}")
print(list_1)
print(list_2)
print(final_list)

            