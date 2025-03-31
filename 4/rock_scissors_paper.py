from random import randint

t = ["Камень", "Бумага", "Ножницы", "Колодец"]

computer = t[randint(0, 3)]
player = False

while True:
    player = input("\nКамень, Ножницы, Бумага, Колодец? > ").strip().capitalize()
    computer = t[randint(0, 3)]
    
    if player not in t:
        print("Некорректный ход! Выберите из списка:", ", ".join(t))
        continue
    
    print(f"Компьютер выбрал: {computer}")
    
    if player == computer:
        print("Ничья!")
    
    # Обработка выбора игрока
    elif player == "Камень":
        if computer == "Бумага" or computer == "Колодец":
            print(f"Ты проиграл! {computer} {'накрывает' if computer == 'Бумага' else 'топит'} {player}")
        else:
            print(f"Ты выиграл! {player} разбивает {computer}")
    
    elif player == "Бумага":
        if computer == "Ножницы" or computer == "Колодец":
            print(f"Ты проиграл! {computer} {'режет' if computer == 'Ножницы' else 'проваливается в'} {player}")
        else:
            print(f"Ты победил! {player} накрывает {computer}")
    
    elif player == "Ножницы":
        if computer == "Камень" or computer == "Колодец":
            print(f"Ты проиграл! {computer} {'разбивает' if computer == 'Камень' else 'топит'} {player}")
        else:
            print(f"Ты выиграл! {player} режет {computer}")
    
    elif player == "Колодец":
        if computer == "Бумага":
            print(f"Ты проиграл! {computer} накрывает {player}")
        else:
            print(f"Ты победил! {player} топит {computer}")