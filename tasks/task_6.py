distance = float(input('Дистанция в первый день: '))
goal = float(input('Конечная цель: '))
days = 1
while distance < goal:
    distance *= 1.1
    days += 1
print(f'До цели нужно: {days} дней ')