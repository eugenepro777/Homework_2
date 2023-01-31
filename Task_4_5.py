'''
Задайте список из N элементов, заполненных числами
из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
Реализуйте алгоритм перемешивания списка.
'''
import random

size = int(input('Введите размер списка (N): '))

test_list = []
for i in range(size):
    test_list.append(random.randint(- size, size))
print('Исходный список:', test_list)

positions = open('file.txt', 'r')
amount = test_list[int(positions.readline())] * test_list[int(positions.readline(2))] 
print('Произведение =', amount)
positions.close()

print()
for i in range(size):
    j = random.randint(0, size - 1)
    temp = test_list[i]
    test_list[i] = test_list[j]
    test_list[j] = temp
print('Перемешанный список: ' + str(test_list))
