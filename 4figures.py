def draw_squre(n):
    for i in range(n):
        for j in range(n):
            print('*', end=" ")
        print()
    print()

def draw_triangle(n):
    for i in range(n):
        for j in range(1, i + 1):
            print('*', end=" ")
        print()

def draw_rhombus(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        print('*' * i, end='')
        print('*' * (i + 1))

    for i in range(1, n):
        print(' ' * (i + 1), end='')
        print('*' * (n - i), end='')
        print('*' * (n - i - 1), )
    print()

def figure():
    m = input('input figure: ')
    n = int(input('input size: '))
    if m == 'square':
        draw_squre(n)
    elif m == 'triangle':
        draw_triangle(n)
    elif m == 'rhombus':
        draw_rhombus(n)




figure()

