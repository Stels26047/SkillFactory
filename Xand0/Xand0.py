table_str1 = ['|1|', '|2|', '|3|']  # поле первой строки
table_str2 = ['|4|', '|5|', '|6|']  # поле второй строки
table_str3 = ['|7|', '|8|', '|9|']  # поле третей строки


'''Поле для ввода X и 0'''


def Game_place():
    print('Игра в крестики нолики'+'\n')
    print("Приветсвую игрока 1 и 2!!!!")
    print()
    print(table_str1[0] + ' ' + table_str1[1] + ' ' + table_str1[2])
    print(table_str2[0] + ' ' + table_str2[1] + ' ' + table_str2[2])
    print(table_str3[0]+' ' + table_str3[1] + ' ' + table_str3[2])
    print()


def Game():
    Game_place()
    filter_references = set()
    pass_1 = 1
    pass_2 = 2
    while len(filter_references) != 9:
        if pass_1 <= 9:

            X = '|X|'  # переменная хранящая будующий X

            '''Проверка в случае ввода не тех данных по X'''
            while True:
                try:
                    print()
                    player_1 = input('Введите цифру клетки для X (1-9): ')
                    filter_references.add(player_1)
                    if type(int(player_1)):
                        if int(player_1) < 1 or int(player_1) > 9:
                            filter_references.remove(player_1)
                            print("Введенное число находится")
                            print('за пределы нумерации.')
                        elif len(filter_references) == pass_1:
                            '''Логика для замены клеток на X'''

                            if player_1 == table_str1[0][1:2]:
                                table_str1.pop(int(player_1) - 1)
                                table_str1.insert(int(player_1) - 1, X)
                            elif player_1 == table_str1[1][1:2]:
                                table_str1.pop(int(player_1) - 1)
                                table_str1.insert(int(player_1) - 1, X)
                            elif player_1 == table_str1[2][1:2]:
                                table_str1.pop(int(player_1) - 1)
                                table_str1.insert(int(player_1) - 1, X)
                            elif player_1 == table_str2[0][1:2]:
                                table_str2.pop(int(player_1) - 4)
                                table_str2.insert(int(player_1) - 4, X)
                            elif player_1 == table_str2[1][1:2]:
                                table_str2.pop(int(player_1) - 4)
                                table_str2.insert(int(player_1) - 4, X)
                            elif player_1 == table_str2[2][1:2]:
                                table_str2.pop(int(player_1) - 4)
                                table_str2.insert(int(player_1) - 4, X)
                            elif player_1 == table_str3[0][1:2]:
                                table_str3.pop(int(player_1) - 7)
                                table_str3.insert(int(player_1) - 7, X)
                            elif player_1 == table_str3[1][1:2]:
                                table_str3.pop(int(player_1) - 7)
                                table_str3.insert(int(player_1) - 7, X)
                            elif player_1 == table_str3[2][1:2]:
                                table_str3.pop(int(player_1) - 7)
                                table_str3.insert(int(player_1) - 7, X)
                            pass_1 += 2
                            break
                        else:
                            print("Введенное число было введено.")
                except ValueError or KeyError:
                    print("Вы ввели либо не целое число,либо не число.")
                    filter_references.remove(player_1)

            '''Поле для ввода данных в поле'''
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

            '''Логика дающий выиграш в случае победы игрока один'''
            if table_str1[0] == '|X|' and table_str1[1] == '|X|':
                if table_str1[2] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str2[0] == '|X|' and table_str2[1] == '|X|':
                if table_str2[2] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str3[0] == '|X|' and table_str3[1] == '|X|':
                if table_str3[2] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str1[0] == '|X|' and table_str2[0] == '|X|':
                if table_str3[0] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str1[1] == '|X|' and table_str2[1] == '|X|':
                if table_str3[1] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str1[2] == '|X|' and table_str2[2] == '|X|':
                if table_str3[2] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str1[0] == '|X|' and table_str2[1] == '|X|':
                if table_str3[2] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break
            elif table_str1[2] == '|X|' and table_str2[1] == '|X|':
                if table_str3[0] == '|X|':
                    print('\n'+'Игрок один выиграл.')
                    break

        if pass_2 <= 8:

            zero = '|0|'  # переменная хранящая будующий 0

            '''Проверка в случае ввода не тех данных по 0'''
            while True:
                try:
                    print()
                    player_2 = input('Введите цифру клетки для 0 (1-9): ')
                    filter_references.add(player_2)
                    if type(int(player_2)):
                        if int(player_2) < 1 or int(player_2) > 9:
                            filter_references.remove(player_2)
                            print("Введенное число находится")
                            print('за пределы нумерации.')
                        elif len(filter_references) == pass_2:
                            '''Логика для замены клеток на 0'''

                            if player_1 == table_str1[0][1:2]:
                                table_str1.pop(int(player_1) - 1)
                                table_str1.insert(int(player_1) - 1, X)
                            elif player_1 == table_str1[1][1:2]:
                                table_str1.pop(int(player_1) - 1)
                                table_str1.insert(int(player_1) - 1, X)
                            elif player_1 == table_str1[2][1:2]:
                                table_str1.pop(int(player_1) - 1)
                                table_str1.insert(int(player_1) - 1, X)
                            elif player_1 == table_str2[0][1:2]:
                                table_str2.pop(int(player_1) - 4)
                                table_str2.insert(int(player_1) - 4, X)
                            elif player_1 == table_str2[1][1:2]:
                                table_str2.pop(int(player_1) - 4)
                                table_str2.insert(int(player_1) - 4, X)
                            elif player_1 == table_str2[2][1:2]:
                                table_str2.pop(int(player_1) - 4)
                                table_str2.insert(int(player_1) - 4, X)
                            elif player_1 == table_str3[0][1:2]:
                                table_str3.pop(int(player_1) - 7)
                                table_str3.insert(int(player_1) - 7, X)
                            elif player_1 == table_str3[1][1:2]:
                                table_str3.pop(int(player_1) - 7)
                                table_str3.insert(int(player_1) - 7, X)
                            elif player_1 == table_str3[2][1:2]:
                                table_str3.pop(int(player_1) - 7)
                                table_str3.insert(int(player_1) - 7, X)
                            if player_2 == table_str1[0][1:2]:
                                table_str1.pop(int(player_2) - 1)
                                table_str1.insert(int(player_2) - 1, zero)
                            elif player_2 == table_str1[1][1:2]:
                                table_str1.pop(int(player_2) - 1)
                                table_str1.insert(int(player_2) - 1, zero)
                            elif player_2 == table_str1[2][1:2]:
                                table_str1.pop(int(player_2) - 1)
                                table_str1.insert(int(player_2) - 1, zero)
                            elif player_2 == table_str2[0][1:2]:
                                table_str2.pop(int(player_2) - 4)
                                table_str2.insert(int(player_2) - 4, zero)
                            elif player_2 == table_str2[1][1:2]:
                                table_str2.pop(int(player_2) - 4)
                                table_str2.insert(int(player_2) - 4, zero)
                            elif player_2 == table_str2[2][1:2]:
                                table_str2.pop(int(player_2) - 4)
                                table_str2.insert(int(player_2) - 4, zero)
                            elif player_2 == table_str3[0][1:2]:
                                table_str3.pop(int(player_2) - 7)
                                table_str3.insert(int(player_2) - 7, zero)
                            elif player_2 == table_str3[1][1:2]:
                                table_str3.pop(int(player_2) - 7)
                                table_str3.insert(int(player_2) - 7, zero)
                            elif player_2 == table_str3[2][1:2]:
                                table_str3.pop(int(player_2) - 7)
                                table_str3.insert(int(player_2) - 7, zero)
                            pass_2 += 2
                            break
                        else:
                            print("Введенное число было введено.")
                except ValueError or KeyError:
                    print("Вы ввели либо не целое число,либо не число.")
                    filter_references.remove(player_2)

            '''Поле для ввода данных в поле'''
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

            '''Логика дающий выиграш в случае победы игрока два'''
            if table_str1[0] == '|0|' and table_str1[1] == '|0|':
                if table_str1[2] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str2[0] == '|0|' and table_str2[1] == '|0|':
                if table_str2[2] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str3[0] == '|0|' and table_str3[1] == '|0|':
                if table_str3[2] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str1[0] == '|0|' and table_str2[0] == '|0|':
                if table_str3[0] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str1[1] == '|0|' and table_str2[1] == '|0|':
                if table_str3[1] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str1[2] == '|0|' and table_str2[2] == '|0|':
                if table_str3[2] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str1[0] == '|0|' and table_str2[1] == '|0|':
                if table_str3[2] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
            elif table_str1[2] == '|0|' and table_str2[1] == '|0|':
                if table_str3[0] == '|0|':
                    print('\n'+'Игрок второй выиграл.')
                    break
    else:
        print()
        print('Нет победителя!')  # Вариант,если нет победителя

Game()
