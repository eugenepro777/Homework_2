'''
Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

'''

n = int(input('Введите число n:  '))
amount = 0

print('Последовательность: ', end="")
for i in range(1, n + 1):
    series = round((1 + 1 / i) ** i, 3)
    print(f'{series}', end=" ")
    amount += series
print(f'\nСумма = {round(amount, 3)}')
