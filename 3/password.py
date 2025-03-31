import random

def generate_password():
    password = []
    # Заглавные буквы (A-Z)
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(65, 90)))
    
    # Строчные буквы (a-z)
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(97, 122)))
    
    # Цифры (0-9)
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(48, 57)))
    
    # Восклицательные знаки
    for _ in range(random.randint(1, 2)):
        password.append('!')
    
    random.shuffle(password)
    return ''.join(password)

# Основной цикл программы
with open('passwords.txt', 'a', encoding='utf-8') as file:
    while True:
        site = input("\nВведите сайт (или 'q' для выхода): ").strip()
        if site.lower() == 'q':
            break
        
        login = input("Введите логин: ").strip()
        password = generate_password()
        
        # Запись в файл
        file.write(f"{site};{login};{password}\n")
        print(f"\nСгенерирован пароль: {password}")
        print("Данные сохранены в файл!")

print("\nРабота программы завершена.")