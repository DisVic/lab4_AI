import time

def fibSequence(n):
    """Итеративная генерация последовательности Фибоначчи"""
    assert n > 0, "n должно быть больше 0"
    series = [1]
    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    return series

def fibRecurse(n):
    """Рекурсивная генерация последовательности Фибоначчи"""
    assert n > 0, "n должно быть больше 0"
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        prev = fibRecurse(n-1)
        return prev + [prev[-1] + prev[-2]]

def measure_time(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start

while True:
    try:
        n = int(input("\nВведите количество чисел Фибоначчи (0 для выхода): "))
        if n == 0:
            break
        if n < 1:
            print("Число должно быть больше 0!")
            continue

        # Измерение времени для итеративной версии
        iter_result, iter_time = measure_time(fibSequence, n)
        
        # Измерение времени для рекурсивной версии
        recurse_result, recurse_time = measure_time(fibRecurse, n)
        
        # Проверка корректности результатов
        assert iter_result == recurse_result, "Результаты не совпадают!"
        
        # Вывод результатов
        print(f"\nРезультат ({n} чисел): {', '.join(map(str, iter_result))}")
        print(f"Итеративная версия: {iter_time:.6f} сек")
        print(f"Рекурсивная версия: {recurse_time:.6f} сек")
        print(f"Разница: {recurse_time - iter_time:.6f}s")

        # if n > 30:
        #     print("\n⚠️ Рекурсивный метод для n > 30 работает очень медленно!")

    except ValueError:
        print("Ошибка: Введите целое число!")
    except RecursionError:
        print("Ошибка: Слишком большая глубина рекурсии!")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

print("\nРабота программы завершена.")