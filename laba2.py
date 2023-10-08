# Основи синтаксису Python 3
print("Hello, world!")

# Змінні та прості типи
name = "John"
age = 30
height = 1.75
is_student = True

# Динамічна типізація
x = 5
print(type(x))  # Вивід типу змінної

# Базові операції та приведення типів
num1 = 10
num2 = "5"
sum_result = num1 + int(num2)

# Тип "List"
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

# Основні оператори
a = 10
b = 5
add_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b

# Форматування стрічок та текстовий вивід
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Робота зі стрічками як зі списками
text = "Hello, world!"
first_char = text[0]
sub_string = text[0:5]

# Тип даних "словник" ("Dictionary")
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])
