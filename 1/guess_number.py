import random

random_number = random.randint(1, 100)
user_won = False
computer_won = False
# Общий диапазон для компьютера и человека
min_range = 1
max_range = 100

print('Я загадал число от 1 до 100. Соревнуйтесь с компьютером, угадайте его первым!')

while not (user_won or computer_won):
    # Ход человека
    user_guess = int(input(f'Ваш ход [{min_range}-{max_range}] > '))
    if user_guess == random_number:
        user_won = True
    else:
        if random_number > user_guess:
            print(f'Больше, чем {user_guess}!')
            min_range = max(min_range, user_guess + 1)  # Обновляем минимум
        else:
            print(f'Меньше, чем {user_guess}!')
            max_range = min(max_range, user_guess - 1)  # Обновляем максимум
    
    if user_won:
        print(f'Вы победили! Загаданное число было {random_number}')
        break
    
    # Ход компьютера (бинарный поиск с учетом новых границ)
    computer_guess = (min_range + max_range) // 2
    print(f'Компьютер предполагает: {computer_guess}')
    if computer_guess == random_number:
        computer_won = True
    else:
        if random_number > computer_guess:
            print(f'Для компьютера: нужно число больше {computer_guess}!')
            min_range = computer_guess + 1
        else:
            print(f'Для компьютера: нужно число меньше {computer_guess}!')
            max_range = computer_guess - 1
    
    if computer_won:
        print(f'Компьютер победил! Загаданное число было {random_number}')
        break