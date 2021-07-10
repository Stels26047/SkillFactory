table_str1 = ['|1|', '|2|', '|3|']  # поле первой строки
table_str2 = ['|4|', '|5|', '|6|']  # поле второй строки
table_str3 = ['|7|', '|8|', '|9|']  # поле третей строки


def Game_place():
    '''Поле для ввода X и 0'''
    print('Игра в крестики нолики'+'\n')
    print("Приветсвую игрока 1 и 2!!!!")
    print(table_str1[0] + ' ' + table_str1[1] + ' ' + table_str1[2])
    print(table_str2[0] + ' ' + table_str2[1] + ' ' + table_str2[2])
    print(table_str3[0]+' ' + table_str3[1] + ' ' + table_str3[2])
    print()


def Game():
    Game_place()
    y = set()
    n = 2
    while len(y) < 7:
        print()
        player_1 = input('Игрок 1 введите цифру клетки для крестика(X)(1-9): ')
        player_2 = input('Игрок 2 введите цифру клетки для нолика(0)(1-9): ')
        y.add(player_1)
        y.add(player_2)
        a = '|X|'  # переменная хранящая будующий X
        b = '|0|'  # переменная хранящая будующий 0

        '''Проверка в случае ввода не тех данных'''
        while True:
            try:
                if type(int(player_1)) and type(int(player_2)):
                    break
            except ValueError:
                print("Вы ввели либо не целое число,либо не число.")
                y.remove(player_1)
                y.remove(player_2)
                break

        if int(player_1) < 1 or int(player_1) > 9:
            y.remove(player_1)
        if int(player_2) < 1 or int(player_2) > 9:
            y.remove(player_2)

        '''Логика для замены клеток на X и 0'''
        if len(y) == n:
            if int(player_1) == 1 or int(player_1) == 2 or int(player_1) == 3:
                table_str1.pop(int(player_1) - 1)
                table_str1.insert(int(player_1) - 1, a)
            elif int(player_1) == 4 or int(player_1) == 5:
                table_str2.pop(int(player_1) - 4)
                table_str2.insert(int(player_1) - 4, a)
            elif int(player_1) == 6:
                table_str2.pop(int(player_1) - 4)
                table_str2.insert(int(player_1) - 4, a)
            elif int(player_1) == 7 or int(player_1) == 8:
                table_str3.pop(int(player_1) - 7)
                table_str3.insert(int(player_1) - 7, a)
            elif int(player_1) == 9:
                table_str3.pop(int(player_1) - 7)
                table_str3.insert(int(player_1) - 7, a)
            if int(player_2) == 1 or int(player_2) == 2 or int(player_2) == 3:
                table_str1.pop(int(player_2) - 1)
                table_str1.insert(int(player_2) - 1, b)
            elif int(player_2) == 4 or int(player_2) == 5:
                table_str2.pop(int(player_2) - 4)
                table_str2.insert(int(player_2) - 4, b)
            elif int(player_2) == 6:
                table_str2.pop(int(player_2) - 4)
                table_str2.insert(int(player_2) - 4, b)
            elif int(player_2) == 7 or int(player_2) == 8:
                table_str3.pop(int(player_2) - 7)
                table_str3.insert(int(player_2) - 7, b)
            elif int(player_2) == 9:
                table_str3.pop(int(player_2) - 7)
                table_str3.insert(int(player_2) - 7, b)
            print()
            n += 2
        else:
            print("Введенное число было введено другим игроком.")
            print("Или введенное число находится за пределы нумерации.")

        '''Циклы выводящии данные таблицы'''
        print()
        for i in table_str1:
            print(i, end=' ')
        print()
        for j in table_str2:
            print(j, end=' ')
        print()
        for k in table_str3:
            print(k, end=' ')
        print()

        '''Логика дающий выиграш в случае победы игрока'''
        if table_str1[0] == '|X|' and table_str1[1] == '|X|':
            if table_str1[2] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str1[0] == '|0|' and table_str1[1] == '|0|':
            if table_str1[2] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str2[0] == '|X|' and table_str2[1] == '|X|':
            if table_str2[2] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str2[0] == '|0|' and table_str2[1] == '|0|':
            if table_str2[2] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str3[0] == '|X|' and table_str3[1] == '|X|':
            if table_str3[2] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str3[0] == '|0|' and table_str3[1] == '|0|':
            if table_str3[2] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str1[0] == '|X|' and table_str2[0] == '|X|':
            if table_str3[0] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str1[0] == '|0|' and table_str2[0] == '|0|':
            if table_str3[0] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str1[1] == '|X|' and table_str2[1] == '|X|':
            if table_str3[1] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str1[1] == '|0|' and table_str2[1] == '|0|':
            if table_str3[1] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str1[2] == '|X|' and table_str2[2] == '|X|':
            if table_str3[2] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str1[2] == '|0|' and table_str2[2] == '|0|':
            if table_str3[2] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str1[0] == '|X|' and table_str2[1] == '|X|':
            if table_str3[2] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str1[0] == '|0|' and table_str2[1] == '|0|':
            if table_str3[2] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
        if table_str1[2] == '|X|' and table_str2[1] == '|X|':
            if table_str3[0] == '|X|':
                print('\n'+'Игрок один выиграл.')
                break
        if table_str1[2] == '|0|' and table_str2[1] == '|0|':
            if table_str3[0] == '|0|':
                print('\n'+'Игрок второй выиграл.')
                break
    else:
        print('\n'+'Нет победителя!')
Game()
