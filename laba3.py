# Функція для перевірки, чи є число простим
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Введення числа від користувача
num = int(input("Введіть ціле число: "))

# Перевірка чи є число простим і виведення результату
if is_prime(num):
    print(f"{num} є простим числом.")
else:
    print(f"{num} не є простим числом.")
