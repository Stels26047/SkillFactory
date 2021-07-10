from random import randint


def guessing_number():

    computer_guess = randint(1, 30)  # компьютер выдает рандомное число
    number_person = int(input("Введите натуральное число: "))
    count = 1

    while True:

        '''Проверка индентичности введенного числа с числом компьютера'''
        if computer_guess != number_person:
            if computer_guess < number_person:
                count += 1
                computer_guess += 1
                print(f'Это наверное число: {computer_guess}')
            elif computer_guess < number_person:
                count += 1
                computer_guess -= 1
                print(f'Это наверное число: {computer_guess}')
        else:
            break

    return f"Было сделано попыток {count}."  # Общие число попыток

print(guessing_number())
