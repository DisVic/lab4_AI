import math

def is_prime(x):
    """Проверяет, является ли число простым."""
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def find_nearest_prime(n):
    """Находит ближайшее простое число к заданному."""
    if is_prime(n):
        return n
    
    # Поиск ближайшего простого в меньшую сторону
    lower = n - 1
    while lower >= 2:
        if is_prime(lower):
            break
        lower -= 1
    
    # Поиск ближайшего простого в большую сторону
    upper = n + 1
    while True:
        if is_prime(upper):
            break
        upper += 1
    
    # Определение ближайшего
    if lower < 2:
        return upper
    return lower if (n - lower) <= (upper - n) else upper

def main():
    """Основной цикл программы."""
    while True:
        user_input = input("\nВведите число (или 'exit' для выхода): ").strip()
        if user_input.lower() in ('exit', 'quit', 'q'):
            break
        try:
            num = int(user_input)
            if is_prime(num):
                print(f" {num} — простое число.")
            else:
                nearest = find_nearest_prime(num)
                print(f" {num} не простое. Ближайшее простое: {nearest}")
        except ValueError:
            print(" Ошибка: введите целое число.")

if __name__ == "__main__":
    main()