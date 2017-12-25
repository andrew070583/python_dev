import random

def random_array(n):
    a = []
    for i in range(n):
        a.append([random.randint(100, 999) for j in range(n)])
    return a

def print_array(a):

    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()

b = random_array(10)
print_array(b)

