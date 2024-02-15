string = input("Введіть рядок: ")
letter_count = 0
digit_count = 0
for character in string:
    if character.isalpha():
        letter_count +=1
    elif character.isdigit():
        digit_count += 1
print("Кількість букв:", letter_count)
print("Кількість цифр:", digit_count)