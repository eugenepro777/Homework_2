'''
Задача 14: Требуется вывести все целые степени
двойки (т.е. числа вида 2^k), не превосходящие числа N.
Пример. 
10 -> 1 2 4 8
'''
N = int(input('Введите число N: '))

power = 0
count = 0
while count < N - power:
    count = 2 ** power
    print(count)
    power += 1
