import os
import time
try:
    from platform import platform
except:
    os.system("pip install platform")
    from platform import platform
try:
    from art import *
except:
    os.system('pip install art')
    from art import *

puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]


if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'


def printart(text):
    os.system(delet)
    print_art = text2art(text)
    print(print_art)

def title():
    printart('HackPD')

def error(text):
    printart("Error")
    print(text)
    time.sleep(3)



x = 0
y = 0

xtest = True
ytest = True

count = 0

while True:

    count += 1

    title()

    if y == 0:
        ytest = True

    if x == 0:
        xtest = True

    if x >= 100:
        xtest = False

    if y >= 20:
        ytest = False

    if xtest == True:
        x += 1
    if xtest == False:
        x -= 1

    if ytest == True:
        y += 1
    if ytest == False:
        y -= 1

    for i in range(21):
        send = "                                                                                                    "
        if i == y:
            send = f"{send[x:]}HACKER{send[:x-6]}"
        print(f"{send}")
    if count >= 100:
        title()
        break



menu = """1: Проверить пароль!
2: Ваши поиски!
3: Об утилите!"""

menu2 = """1: Полная проверка!
2: Поверхностная проверка!"""

menu3 = """1: Показывать пароли!
2: Не показывать пароли!"""

while True:
    try:
        title()
        print(menu)
        number = int(input("Введите число: "))
        if number == 1:
            title()
            user = input("Введите свой пароль: ")
            title()
            print(menu2)
            number = int(input("Введите число: "))
            if number == 1:
                title()
                print(menu3)
                number = int(input("Введите число: "))
                title()
                test_print = False
                if number == 1:
                    test_print = True
                hack = 0
                search = False
                reason = ''
                try:
                    user = int(user)
                    hack += 1
                    reason = reason + 'Пароль состоит из цифр. '
                    user = str(user)
                except ValueError:
                    pass
                if len(user) < 10:
                    hack += 1
                    reason = reason + 'Пароль меньше 10 символов. '
                if user[len(user) - 3:len(user)] == '123':
                    hack += 1
                    reason = reason + 'Не употребляйте конец пароля как "123". '
                count = 0
                file = open(f"passwords{dr}password.txt", "r", encoding="utf-8")
                for i in file:
                    count += 1
                    i = i.replace('\n', '')
                    if test_print == True:
                        print(f"Попытка: {count}, пароль: {i}")
                    if i == user:
                        title()
                        reason = reason + 'Был найден в базе данных. '
                        print(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                        file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                        file1.write(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                        file1.close()
                        time.sleep(10)
                        search = True
                        break
                if search == False:
                    file = open(f"passwords{dr}usernames.txt", "r", encoding="utf-8")
                    for i in file:
                        count += 1
                        i = i.replace('\n', '')
                        if test_print == True:
                            print(f"Попытка: {count}, пароль: {i}")
                        if i == user:
                            title()
                            reason = reason + 'Был найден в базе данных. '
                            print(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                            file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                            file1.write(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                            file1.close()
                            time.sleep(10)
                            search = True
                            break
                    if search == False:
                        file = open(f"passwords{dr}wifipwd.txt", "r", encoding="utf-8")
                        for i in file:
                            count += 1
                            i = i.replace('\n', '')
                            if test_print == True:
                                print(f"Попытка: {count}, пароль: {i}")
                            if i == user:
                                title()
                                reason = reason + 'Был найден в базе данных. '
                                print(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                                file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                                file1.write(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                                file1.close()
                                time.sleep(10)
                                search = True
                                break
                        if search == False:
                            if hack >= 1:
                                title()
                                print(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}')
                                file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                                file1.write(f'Пароль: {user} - не безопасен! Причин(ы/а): {reason}\n')
                                file1.close()
                                time.sleep(10)
                            else:
                                file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                                file1.write(f'Пароль: {user} - безопасен, он соответствует нашим нормам!\n')
                                file1.close()

                
            if number == 2:
                number = 0
                hack = 0
                reason = ''
                try:
                    user = int(user)
                    hack += 1
                    reason = reason + 'Пароль состоит из цифр. '
                    user = str(user)
                except ValueError:
                    pass
                if len(user) < 10:
                    hack += 1
                    reason = reason + 'Пароль меньше 10 символов. '
                if user[len(user) - 3:len(user)] == '123':
                    hack += 1
                    reason = reason + 'Не употребляйте конец пароля как "123". '
                if hack >= 1:
                    title()
                    print(f'Ваш пароль не безопасен! Причин(ы/а): {reason}')
                    file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                    file1.write(f'Ваш пароль не безопасен! Причин(ы/а): {reason}\n')
                    file1.close()
                    time.sleep(10)
                else:
                    title()
                    print('Пароль безопасен, он соответствует нашим нормам!')
                    file1 = open(f"passwords{dr}test_passwords.txt", "a", encoding="utf-8")
                    file1.write(f'Пароль: {user} - безопасен, он соответствует нашим нормам!\n')
                    file1.close()
                    time.sleep(10)
        if number == 2:
            title()
            number = int(input('Выберите кол-во секунд для просмотра ваших поисков: '))
            file = open(f"passwords{dr}test_passwords.txt", "r", encoding="utf-8")
            title()
            for i in file:
                i = i.replace('\n', '')
                print(i)
            time.sleep(number)
        if number == 3:
            title()
            print('Создано: @MasterKomand!\nКоманда: HackerRullerTools\nСоздано для "хороших целей"!')
            time.sleep(5)
    except ValueError:
        error("Вы должны были выбрать число!")
        title()
        print(menu)
