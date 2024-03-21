from random import choice
def chooise_it(bot=False):
    if bot:
        return choice({'к', 'н', 'п'})
    else:
        while True:
            choice = input('Введіть свій вибір к н або п)