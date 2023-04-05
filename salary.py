def calculate_salary():
    print('Расчет заработной платы')
    a = int(input('Введите ежедневный оклад: '))
    d = int(input('Введите количество отработанных дней: '))
    s = a * d / 100 * 87
    print(s)
calculate_salary()