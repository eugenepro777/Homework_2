'''
Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной
 и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
Пример: 5 -> 1 0 1 1 0
2
'''
import random

size = int(input('Введите количество монет: '))

test_list = []
for i in range(size):
    test_list.append(random.randint(0, 1))
print('Как легли монеты:', test_list)

mini = 0
for i in test_list:
    if bool(i) == False:
        mini += 1
print('Надо перевернуть: ', mini)
