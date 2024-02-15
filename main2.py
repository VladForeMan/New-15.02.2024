string = input("Введіть рядок: ")
reversed_string = ""
for character in string:
    reversed_string = character + reversed_string
print("Розгорнутий рядок", reversed_string)