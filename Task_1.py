'''
Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''

number_in = input('Введите число: ')

if float(number_in) < 0:                            
    number_in = float(number_in) * (-1)

amount = 0
for i in str(number_in):
    if i != '.':
        amount += int(i)

print(f'Сумма чисел = {amount}')

