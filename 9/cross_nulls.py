def play_3x3_vs_ai():
    # Инициализация поля 3x3 с использованием строк
    board = [str(i) for i in range(1, 10)]
    
    def draw_board():
        print("\n" + "-" * 13)
        for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
            print("-" * 13)
    
    def ai_move():
        import random
        # Поиск выигрышного хода для ИИ
        for cell in range(9):
            if board[cell] in "123456789":
                original = board[cell]
                board[cell] = "O"
                if check_win() == "O":
                    return
                board[cell] = original
        
        # Блокировка выигрышных ходов игрока
        for cell in range(9):
            if board[cell] in "123456789":
                original = board[cell]
                board[cell] = "X"
                if check_win() == "X":
                    board[cell] = "O"
                    return
                board[cell] = original
        
        # Случайный ход
        empty_cells = [i for i in range(9) if board[i] in "123456789"]
        if empty_cells:
            board[random.choice(empty_cells)] = "O"
    
    def check_win():
        win_lines = [(0,1,2), (3,4,5), (6,7,8),
                    (0,3,6), (1,4,7), (2,5,8),
                    (0,4,8), (2,4,6)]
        for line in win_lines:
            if board[line[0]] == board[line[1]] == board[line[2]]:
                return board[line[0]]
        return False
    
    # Игровой цикл
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            # Ход человека
            while True:
                try:
                    cell = int(input("Ваш ход (1-9): "))
                    if 1 <= cell <= 9 and board[cell-1] in "123456789":
                        board[cell-1] = "X"
                        break
                    print("Некорректный ввод!")
                except: 
                    print("Введите число от 1 до 9!")
        else:
            # Ход ИИ
            ai_move()
        
        winner = check_win()
        if winner:
            draw_board()
            print("Вы выиграли!" if winner == "X" else "Компьютер выиграл!")
            break
        if counter == 8:
            draw_board()
            print("Ничья!")
            break
        counter += 1

def play_5x5_two_players():
    # Инициализация поля 5x5
    board = list(range(1, 26))
    
    def draw_board():
        print("\n" + "-" * 26)
        for i in range(5):
            row = "| " + " | ".join(f"{cell:2}" for cell in board[i*5:(i+1)*5]) + " |"
            print(row)
            print("-" * 26)
    
    def check_win(b):
        # Проверка всех возможных линий
        size = 5
        # Горизонтали
        for i in range(size):
            for j in range(size - 4):
                if b[i*5+j] == b[i*5+j+1] == b[i*5+j+2] == b[i*5+j+3] == b[i*5+j+4] and b[i*5+j] in "XO":
                    return b[i*5+j]
        
        # Вертикали
        for i in range(size - 4):
            for j in range(size):
                if b[i*5+j] == b[(i+1)*5+j] == b[(i+2)*5+j] == b[(i+3)*5+j] == b[(i+4)*5+j] and b[i*5+j] in "XO":
                    return b[i*5+j]
        
        # Диагонали
        for i in range(size - 4):
            for j in range(size - 4):
                if b[i*5+j] == b[(i+1)*5+j+1] == b[(i+2)*5+j+2] == b[(i+3)*5+j+3] == b[(i+4)*5+j+4] and b[i*5+j] in "XO":
                    return b[i*5+j]
                if b[i*5+j+4] == b[(i+1)*5+j+3] == b[(i+2)*5+j+2] == b[(i+3)*5+j+1] == b[(i+4)*5+j] and b[i*5+j+4] in "XO":
                    return b[i*5+j+4]
        return False
    
    # Игровой цикл
    counter = 0
    while True:
        draw_board()
        player = "X" if counter % 2 == 0 else "O"
        while True:
            try:
                cell = int(input(f"Игрок {player} (1-25): "))
                if 1 <= cell <= 25 and str(board[cell-1]) not in "XO":
                    board[cell-1] = player
                    break
                print("Некорректный ввод!")
            except: pass
        
        winner = check_win(board)
        if winner:
            draw_board()
            print(f"Игрок {winner} выиграл!")
            break
        if counter == 24:
            draw_board()
            print("Ничья!")
            break
        counter += 1

# Выбор режима игры
print("1 - Игра 3x3 против компьютера")
print("2 - Игра 5x5 для двух игроков")
choice = input("Выберите режим: ")

if choice == "1":
    play_3x3_vs_ai()
elif choice == "2":
    play_5x5_two_players()
else:
    print("Некорректный выбор!")

input("\nНажмите Enter для выхода...")