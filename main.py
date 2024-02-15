min_value = int(input("Введіть першу межу діапазону: "))
max_value = int(input("Введіть другу межу діапазону: "))
while True:
    number = int(input("Введіть число: "))
    if min_value <= number <= max_value:
        break
    print("Число не входить в діапазон. Повторіть введення")