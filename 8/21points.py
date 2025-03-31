import random
import os
import time

# Инициализация переменных
player_score = 0
bot_score = 0
player_cards = []
bot_cards = []
all_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Ввод уровня сложности
difficulty = float(input("Введите уровень сложности бота (0-1): "))
while difficulty < 0 or difficulty > 1:
    print("Некорректное значение! Введите число от 0 до 1.")
    difficulty = float(input("Уровень сложности бота: "))

def show_status():
    """Отображает текущее состояние игры"""
    os.system('cls')
    print("="*40)
    print(f"Ваши карты: {player_cards} | Сумма: {player_score}")
    print(f"Карты бота: {' '.join('?'*len(bot_cards))} | Сумма: {bot_score}")
    print("="*40 + "\n")

# Основной цикл игры
print("Игра начинается! Нажмите Enter.")
input()

while True:
    show_status()
    
    # Проверка условий для игрока
    if player_score == 21:
        print("Blackjack! Вы победили!")
        break
    if player_score > 21:
        print("Перебор! Вы проиграли.")
        break

    # Ход игрока
    choice = input("Брать карту? (yes/no): ").lower()
    if choice == 'yes':
        card = random.choice(all_cards)
        player_cards.append(card)
        player_score += card
        print(f"Вы взяли: {card}")
        time.sleep(1)
    elif choice == 'no':
        # Ход бота с полным раскрытием карт
        print("="*40)
        print(f"Карты бота: {bot_cards} | Сумма: {bot_score}")
        
        while True:
            # Логика бота
            rand_num = random.random()
            if bot_score >= 21:
                break
                
            if rand_num > difficulty:
                card = random.choice(all_cards)
            else:
                needed = (21 - bot_score)
                possible = [c for c in all_cards if c <= needed]
                card = max(possible) if possible else 0
            
            if card == 0 or bot_score >= 17:
                print("Бот пропускает ход")
                break
            else:
                bot_cards.append(card)
                bot_score += card
                print(f"Бот взял: {card}")
                time.sleep(1)
        
        # Итоговые проверки
        show_status()
        if bot_score > 21 or player_score > bot_score:
            print("Вы победили!")
        elif bot_score > player_score:
            print("Вы проиграли!")
        else:
            print("Ничья!")
        break
    else:
        print("Ошибка ввода!")
        time.sleep(1)

input("\nНажмите Enter для выхода...")