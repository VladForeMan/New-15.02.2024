string = input("Введіть рядок: ")
symbol = input("Введіть символ: ")
symbol_count = 0
for character in string:
  if character == symbol:
    symbol_count += 1