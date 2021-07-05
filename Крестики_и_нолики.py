table_str1 =['|1|','|2|','|3|']#поле первой строки
table_str2 =['|4|','|5|','|6|']#поле второй строки
table_str3 =['|7|','|8|','|9|']#поле третей строки
print('Игра в крестики нолики'+'\n')
print(table_str1[0]+' '+table_str1[1] +' '+table_str1[2] + '\n' + table_str2[0]+' '+table_str2[1] +' '+table_str2[2] + '\n' + table_str3[0]+' '+table_str3[1] +' '+table_str3[2])#пустая таблица для крестиков и ноликов
print()

def Game():
    y = set()
    n=2
    while len(y)<7:
        print()
        player_1 = int(input('Игрок 1 введите цифру клетки для крестика(X)(1-9): '))
        y.add(player_1)
        player_2 = int(input('Игрок 2 введите цифру клетки для нолика(0)(1-9): '))
        y.add(player_2)
        a=str(table_str1[1][0:1]) + 'X' + str(table_str1[1][2])#переменная хранящая будующий X
        b=str(table_str2[1][0:1]) + '0' + str(table_str2[1][2])#переменная хранящая будующий 0
        '''Логика для замены клеток на X и 0'''
        if len(y) == n:
            if player_1 == 1 or player_1 == 2 or player_1 == 3:
                table_str1.pop(player_1-1)
                table_str1.insert(player_1-1,a)
            elif player_1 == 4 or player_1 == 5 or player_1 == 6:
                table_str2.pop(player_1 - 4)
                table_str2.insert(player_1 - 4,a)
            elif player_1 == 7 or player_1 == 8 or player_1 == 9:
                table_str3.pop(player_1 - 7)
                table_str3.insert(player_1 - 7,a)
            if player_2 == 1 or player_2 == 2 or player_2 == 3:
                table_str1.pop(player_2 - 1)
                table_str1.insert(player_2 - 1,b)
            elif player_2 == 4 or player_2 == 5 or player_2 == 6:
                table_str2.pop(player_2 - 4)
                table_str2.insert(player_2 - 4,b)
            elif player_2 == 7 or player_2 == 8 or player_2 == 9:
                table_str3.pop(player_2 - 7)
                table_str3.insert(player_2 - 7,b)
            print()
            n+=2
        '''Циклы выводящии данные таблицы'''
        for i in table_str1:
            print(i,end=' ')
        print()
        for j in table_str2:
            print(j,end=' ')
        print()
        for k in table_str3:
            print(k,end=' ')
        '''Логика дающий выиграш в случае победы игрока'''
        if table_str1[0] == '|X|' and table_str1[1] == '|X|' and table_str1[2] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str1[0] == '|0|' and table_str1[1] == '|0|' and table_str1[2] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str2[0] == '|X|' and table_str2[1] == '|X|' and table_str2[2] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str2[0] == '|0|' and table_str2[1] == '|0|' and table_str2[2] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str3[0] == '|X|' and table_str3[1] == '|X|' and table_str3[2] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str3[0] == '|0|' and table_str3[1] == '|0|' and table_str3[2] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str1[0] == '|X|' and table_str2[0] == '|X|' and table_str3[0] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str1[0] == '|0|' and table_str2[0] == '|0|' and table_str3[0] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str1[1] == '|X|' and table_str2[1] == '|X|' and table_str3[1] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str1[1] == '|0|' and table_str2[1] == '|0|' and table_str3[1] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str1[2] == '|X|' and table_str2[2] == '|X|' and table_str3[2] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str1[2] == '|0|' and table_str2[2] == '|0|' and table_str3[2] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str1[0] == '|X|' and table_str2[1] == '|X|' and table_str3[2] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str1[0] == '|0|' and table_str2[1] == '|0|' and table_str3[2] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
        if table_str1[2] == '|X|' and table_str2[1] == '|X|' and table_str3[0] == '|X|':
            print('\n'+'Игрок один выиграл')
            break
        if table_str1[2] == '|0|' and table_str2[1] == '|0|' and table_str3[0] == '|0|':
            print('\n'+'Игрок второй выиграл')
            break
    else:
        print('\n'+'Нет победителя!')
Game()