# def fa_pow(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * fa_pow(x, n - 1)
#
# print(fa_pow(2, 3))
# print(fa_pow(5, 2))
# print(fa_pow(-2, 3))
'''______________________________________________________________'''
def fa_pow(x, n):
    if n == 0:
        return 1
    return x * fa_pow(x, n - 1)

print(fa_pow(2, 3))
print(fa_pow(5, 2))
print(fa_pow(-2, 3))