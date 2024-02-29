# list_nums = [1, -2, 3, -4, 5, -6]
# negatives = 0
# for num in list_nums:
#     if num < 0:
#         negatives += num
# print(f"Сума від'ємних чисел: {sum_negatives}")

# list_nums = [1, 2, 3, 4, 5, 6]
# even = 0
# for num in list_nums:
#     if num % 2 == 0:
#         even += num
# print(f"Сума парних чисел: {sum_even}")

# list_nums = [1, 2, 3, 4, 5, 6]
# odd = 0
# for num in list_nums:
#     if num % 2 != 0:
#         odd += num
# print(f"Сума непарних чисел: {sum_odd}")

# list_nums = [1, 2, 3, 4, 5, 6]
# product_by_3 = 1
# for i, num in enumerate(list_nums):
#     if i % 3 == 0:
#         product_by_3 *= num
# print(f"Добуток елементів з індексами кратними 3: {product_by_3}")

list_nums = [1, 2, 3, 4, 5, 6]
min_num = max_num = list_nums[0]
product = 1
for num in list_nums:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num
for num in list_nums:
    if min_num < num < max_num:
        product *= num
print(f"Добуток елементів між мінімальним і максимальним елементом: {product}")