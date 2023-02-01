""" Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

number = int(input('Введите трёхзначное число: '))

if number > 99 and number < 1000:
    first = number // 100
    second = number // 10 % 10
    third = number % 10
    sum = first+second+third
    print(f'Сумма цифр этого трехзначного числа ->', sum)
    print()
else:
    print('Вы ввели не трёхзначное число!')
    print()
