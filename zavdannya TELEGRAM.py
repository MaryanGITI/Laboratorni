# Зчитування двох чисел з консолі
a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))

# 1. Сума чисел a і b помножена на їх добуток
result1 = (a + b) * (a * b)
if result1 > 100:
    print(result1)
else:
    print("no")

# 2. Сума чисел a і b помножена на їх різницю
result2 = (a + b) * (a - b)
if result2 > 100:
    print(result2)
else:
    print(result2 * 2)

# 3. Сума чисел a і b помножена на їх добуток
result3 = (a + b) * (a * b)
if result3 != 100:
    print(result3)
else:
    print(result3 * 2 if result3 < 5 else result3)

# 4. Сума чисел a і b поділена на b
result4 = (a + b) / b
if result4 != 45:
    print(result4)
else:
    print(result4 * 2 if result4 < 100 else result4)

# 5. Сума чисел a і b поділена на a
result5 = (a + b) / a
if result5 > 100:
    print("yes")
elif result5 != 10:
    print("no")
