# Оголошення класу
class Car:
    # Конструктор класу
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Метод для запуску автомобіля
    def start(self):
        if not self.is_running:
            print(f"{self.make} {self.model} розпочав рух.")
            self.is_running = True
        else:
            print(f"{self.make} {self.model} вже запущений.")

    # Метод для зупинки автомобіля
    def stop(self):
        if self.is_running:
            print(f"{self.make} {self.model} зупинився.")
            self.is_running = False
        else:
            print(f"{self.make} {self.model} вже зупинений.")

    # Метод для отримання інформації про автомобіль
    def info(self):
        status = "запущений" if self.is_running else "зупинений"
        return f"{self.year} {self.make} {self.model}, стан: {status}"

# Створення об'єкту класу Car
my_car = Car("Toyota", "Camry", 2022)

# Виклик методів об'єкту
print(my_car.info())  # Виводимо інформацію про автомобіль
my_car.start()        # Запускаємо автомобіль
my_car.stop()         # Зупиняємо автомобіль
my_car.start()        # Запускаємо автомобіль знову
