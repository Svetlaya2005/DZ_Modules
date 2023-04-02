import salary
import people

print("Хорошего дня, пользователь!")
for t in reversed(range(3)):
    password = int(input("Введите пароль:"))
    if password == 123:
        print('Пароль верный, вход выполнен')
        break
    print('Неправильный пароль, осталось попыток :', t)

