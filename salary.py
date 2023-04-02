print('Расчет заработной платы')
def calculate_salary(self):
    a = int(input('Введите ежедневный оклад: '))
    d = int(input('Введите количество отработанных дней): '))
    n = 0.87
    s = a * d * n
    return(print(s))


