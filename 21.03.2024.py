def function(count):
    if count <=0:
        return
    print(f'hi {count}')
    function(count-1)
    print(f'bye {count}')

function(5)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(f'{factorial(5)=}')
