table_str1 = ['|1|', '|2|', '|3|']  # поле первой строки
table_str2 = ['|4|', '|5|', '|6|']  # поле второй строки
table_str3 = ['|7|', '|8|', '|9|']  # поле третей строки


'''Поле для ввода X и 0'''


def Game_place():
    print('Игра в крестики нолики'+'\n')
    print("Приветсвую игрока 1 и 2!!!!")
    print(table_str1[0] + ' ' + table_str1[1] + ' ' + table_str1[2])
    print(table_str2[0] + ' ' + table_str2[1] + ' ' + table_str2[2])
    print(table_str3[0]+' ' + table_str3[1] + ' ' + table_str3[2])
    print()


def Game():
    Game_place()
    filter_references = set()
    true_input = 2
    while len(filter_references) < 7:
        print()
        player_1 = input('Игрок 1 введите цифру клетки для крестика(X)(1-9): ')
        player_2 = input('Игрок 2 введите цифру клетки для нолика(0)(1-9): ')
        filter_references.add(player_1)
        filter_references.add(player_2)
        X = '|X|'  # переменная хранящая будующий X
        zero = '|0|'  # переменная хранящая будующий 0

        '''Проверка в случае ввода не тех данных'''
        while True:
            try:
                if type(int(player_1)) and type(int(player_2)):
                    break
            except ValueError:
                print("Вы ввели либо не целое число,либо не число.")
                filter_references.remove(player_1)
                filter_references.remove(player_2)
                break

        if int(player_1) < 1 or int(player_1) > 9:
            filter_references.remove(player_1)
        if int(player_2) < 1 or int(player_2) > 9:
            filter_references.remove(player_2)

        '''Логика для замены клеток на X и 0'''
        if len(filter_references) == true_input:
            if int(player_1) == 1 or int(player_1) == 2 or int(player_1) == 3:
                table_str1.pop(int(player_1) - 1)
                table_str1.insert(int(player_1) - 1, X)
            elif int(player_1) == 4 or int(player_1) == 5:
                table_str2.pop(int(player_1) - 4)
                table_str2.insert(int(player_1) - 4, X)
            elif int(player_1) == 6:
                table_str2.pop(int(player_1) - 4)
                table_str2.insert(int(player_1) - 4, X)
            elif int(player_1) == 7 or int(player_1) == 8:
                table_str3.pop(int(player_1) - 7)
                table_str3.insert(int(player_1) - 7, X)
            elif int(player_1) == 9:
                table_str3.pop(int(player_1) - 7)
                table_str3.insert(int(player_1) - 7, X)
            if int(player_2) == 1 or int(player_2) == 2 or int(player_2) == 3:
                table_str1.pop(int(player_2) - 1)
                table_str1.insert(int(player_2) - 1, zero)
            elif int(player_2) == 4 or int(player_2) == 5:
                table_str2.pop(int(player_2) - 4)
                table_str2.insert(int(player_2) - 4, zero)
            elif int(player_2) == 6:
                table_str2.pop(int(player_2) - 4)
                table_str2.insert(int(player_2) - 4, zero)
            elif int(player_2) == 7 or int(player_2) == 8:
                table_str3.pop(int(player_2) - 7)
                table_str3.insert(int(player_2) - 7, zero)
            elif int(player_2) == 9:
                table_str3.pop(int(player_2) - 7)
                table_str3.insert(int(player_2) - 7, zero)
            print()
            true_input += 2
        else:
            print("Введенное число было введено другим игроком.")
            print("Или введенное число находится за пределы нумерации.")

        '''Циклы выводящии данные таблицы'''
        print()
        for element in table_str1:
            print(element, end=' ')
        print()
        for element in table_str2:
            print(element, end=' ')
        print()
        for element in table_str3:
            print(element, end=' ')
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
