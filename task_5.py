earning = int(input('Выручка: '))
costs = int(input('Издержки: '))

if costs > earning:
    print('Убыток')
elif costs < earning:
    print('Прибыль')
    profit = (earning - costs) / earning
    print(f"Рентабельность: {profit}")
    empl_amount = int(input('Количество сотрудников: '))
    profit_per_empl = (earning - costs) / empl_amount
    print(f'Прибыль на одного сотрудника: {profit_per_empl}' )

