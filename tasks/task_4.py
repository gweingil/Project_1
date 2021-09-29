n = int(input('Введите любое целое число: '))
n_max = 0
while n > 0:
    if n % 10 > n_max:
        n_max = n % 10
        if n_max == 9:
            break

    n = n // 10

print(f'Самая большая цифра числа: {n_max}' )
