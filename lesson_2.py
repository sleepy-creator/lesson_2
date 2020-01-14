'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

a = 0
for i in range(1,6):
    a += 1
    print(a,'String = 0')
print('')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
sum = 0
for i in range(10):
    answer = int(input('Введите цифру: '))
    if answer == 5:
        sum += 1

print('Количество цифр пять равно', sum)
print('')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

sum = 0

for i in range(1,101):
     sum+=i
print(sum)
print('')
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
a = 1
for i in range(1,11):
    a *= i
print(a)
print('')
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 2020



while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10
print('')
'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = 545614
sum = 0
while integer_number > 0:
    sum += integer_number % 10
    integer_number = integer_number // 10
print(sum)
print('')
'''
Задача 7
Найти произведение цифр числа.
'''
integer_number = 5451
sum = 1
while integer_number > 0:
    sum *= integer_number % 10
    integer_number = integer_number // 10
print(sum)
print('')
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 84645
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
print('')
'''
Задача 9
Найти максимальную цифру в числе
'''


'''
Задача 10
Найти количество цифр 5 в числе
'''