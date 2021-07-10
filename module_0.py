from random import randint

'''Проверка индентичности введенного числа с числом компьютера'''


def guessing_number(number_person):

    sum = 0
    '''Делает 1000 попыток и выводит за сколько попыток угадал алгоритм'''
    '''И угадывает средние значение этих попыток'''
    for number in range(1, 1001):
        computer_guess = randint(1, 100)  # компьютер выдает рандомное число
        attempt = 0
        while computer_guess != number_person:
            if computer_guess < number_person:
                attempt += 1
                computer_guess += 1
            elif computer_guess > number_person:
                attempt += 1
                computer_guess -= 1
            else:
                break

        print(f"Было сделано попыток {attempt}")  # Общие число попыток
        sum += attempt

    print(f'Средние значение угадывания: {sum / 1000}')

guessing_number(20)
