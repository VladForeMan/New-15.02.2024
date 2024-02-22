while True:
    system = input("Введіть систему оцінювання (1 - 12-бальна,):  ")
    if system in ("1",):
        break
    print("Невірний формат. Спробуйте ще раз.")

grades = []
while True:
    grade = input("Введіть оцінку (0 - для завершення): ")
    if grade == "0":
        break

    if system == "1":
        if not grade.isdigit() or int(grade) < 1 or int(grade) > 12:
            print("Невірний формат оцінки. Спробуйте ще раз.")
            continue
    grades.append(int(grade))

print("Список введених оцінок:")
for grade in grades:
    print(grade)
