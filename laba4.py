# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

# Функція, яка приймає "callback" та викликає його
def apply_callback(callback, x, y):
    result = callback(x, y)
    return result

# Функція, яка додає два числа
def add(x, y):
    return x + y

# Функція, яка віднімає два числа
def subtract(x, y):
    return x - y

# Функція, яка множить два числа
def multiply(x, y):
    return x * y

# Використання "callback" функції apply_callback
result1 = apply_callback(add, 5, 3)
print("Додавання: ", result1)

result2 = apply_callback(subtract, 8, 4)
print("Віднімання: ", result2)

result3 = apply_callback(multiply, 6, 2)
print("Множення: ", result3)
