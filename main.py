import random


top_of_range = input("Введите число: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Введите число больше нуля')
        quit()
else:
    print('Введите цифру в следующий раз')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('сделать предположение: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Введите цифру в следующий раз')
        continue

    if user_guess == random_number:
        print('Ты угадал!!!')
        break
    elif user_guess > random_number:
        print('Число меньше')
    else:
        print('Число больше')

print('У тебя получилось, ты угадал с', guesses, 'раз')
