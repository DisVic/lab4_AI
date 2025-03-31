def calc(a, b, op):
    operations = {
        '+': (lambda a, b: a + b, ' + '),
        '-': (lambda a, b: a - b, ' - '),
        '*': (lambda a, b: a * b, ' × '),
        '/': (lambda a, b: a / b, ' ÷ '),
        '^': (lambda a, b: a ** b, ' ^ '),
        '%': (lambda a, b: (a / 100) * b, '% от '),
        '√': (lambda a, b: b ** (1 / a), f' корень степени {a} из ')
    }
    
    if op not in operations:
        return 'Ошибка: некорректная операция!'
    
    # Специальные проверки
    if op == '/':
        if b == 0:
            return 'Ошибка: деление на ноль!'
    
    if op == '√':
        if a == 0:
            return 'Ошибка: степень корня не может быть нулем!'
        if b < 0:
            if not (a.is_integer() and int(a) % 2 != 0):
                return 'Ошибка: корень четной степени из отрицательного числа!'
    
    try:
        func, symbol = operations[op]
        result = func(a, b)
        
        if op == '%':
            return f'{a}% от {b} = {result}'
        elif op == '√':
            return f'Корень степени {a:.0f} из {b} = {result:.3f}'
        else:
            return f'{a}{symbol}{b} = {result}'
    
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль!'
    except OverflowError:
        return 'Ошибка: слишком большой результат!'
    except ValueError as e:
        return f'Ошибка: {str(e)}'

def main():
    print("Калькулятор с поддержкой операций: +, -, *, /, ^, %, √")
    try:
        a = float(input("Введите первое число: "))
        op = input("Выберите операцию: ")
        
        if op == '%':
            b = float(input("Введите число для вычисления процента: "))
        elif op == '√':
            b = float(input("Введите подкоренное число: "))
        else:
            b = float(input("Введите второе число: "))
        
        print(calc(a, b, op))
    
    except ValueError:
        print("Ошибка: введите корректные числа!")

if __name__ == '__main__':
    main()