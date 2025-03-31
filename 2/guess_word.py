import random

list_of_words = [
    'яблоко', 'победа', 'программирование', 'терминал', 'ноутбук',
    'клавиатура', 'мышь', 'монитор', 'система', 'процессор', 'дисплей',
    'сеть', 'сервер', 'файл', 'папка', 'курсор', 'алгоритм',
    'база данных', 'интерфейс', 'приложение'
]

russian_freq = [
    'о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д',
    'п', 'у', 'я', 'ы', 'ь', 'г', 'з', 'б', 'ч', 'й', 'х', 'ж', 'ш',
    'ю', 'ц', 'щ', 'э', 'ф', 'ъ', 'ё'
]

random_word = random.choice(list_of_words).lower()
set_of_symbols = set(random_word)
discovered_symbols = set()
used_symbols = set()
current_player = 'human'  # Фиксированный первый ход человека

print(f'Загаданное слово: {"_ " * len(random_word)}')
print(f'Длина слова: {len(random_word)} букв.')
print('Первым ходит человек.')

while True:
    if current_player == 'human':
        # Ход человека
        print('\n' + '=' * 30)
        user_symbol = input('Ваш ход > ').lower()
        
        # Валидация ввода
        if len(user_symbol) != 1 or not user_symbol.isalpha() or user_symbol not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Ошибка! Введите одну русскую букву.')
            continue
            
        if user_symbol in used_symbols:
            print('Эта буква уже использовалась!')
            continue
            
        used_symbols.add(user_symbol)
        
        if user_symbol in set_of_symbols:
            print('Верно! Буква есть в слове.')
            discovered_symbols.add(user_symbol)
            if discovered_symbols == set_of_symbols:
                print('\nВы победили! Слово:', random_word)
                break
            progress = ' '.join([ch if ch in discovered_symbols else '_' for ch in random_word])
            print(f'\nСлово: {progress}')
            continue  # Человек продолжает ход
        else:
            print('Неверно!')
            current_player = 'computer'  # Передача хода
        
    else:
        # Ход компьютера
        print('\n' + '=' * 30)
        print('Ход компьютера...')
        
        available_letters = [ch for ch in russian_freq if ch not in used_symbols]
        if not available_letters:
            print('Все буквы использованы. Игра завершена.')
            break
        
        computer_symbol = available_letters[0]
        print(f'Компьютер выбирает букву: {computer_symbol}')
        used_symbols.add(computer_symbol)
        
        if computer_symbol in set_of_symbols:
            print('Компьютер угадал!')
            discovered_symbols.add(computer_symbol)
            if discovered_symbols == set_of_symbols:
                print('\nКомпьютер победил! Слово:', random_word)
                break
            progress = ' '.join([ch if ch in discovered_symbols else '_' for ch in random_word])
            print(f'\nСлово: {progress}')
            continue  # Компьютер продолжает ход
        else:
            print('Компьютер ошибся!')
            current_player = 'human'  # Передача хода
    
    # Обновление прогресса после смены хода
    progress = ' '.join([ch if ch in discovered_symbols else '_' for ch in random_word])
    print(f'\nСлово: {progress}')

if discovered_symbols != set_of_symbols:
    print('\nИгра завершена. Слово не угадано:', random_word)