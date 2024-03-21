#№2
# def sum_range(a, b):
#     if a > b:
#         return 0
#     else:
#         return a + sum_range(a + 1, b)
#
# a = int(input('Введіть початок число: '))
# b = int(input('Введіть кінець число: '))
# print(f'Сума чисел у діапазоні від {a} до {b} дорівнює {sum_range(a, b)}')


def print_stars(n):
    if n == 0:
        return
    else:
        print("*", end="")
        print_stars(n-1)

n = int(input("Введіть кількість зірок: "))
print_stars(n)