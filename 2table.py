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

h = random_array(10)
print_array(h)

print()

for row in h:
    print(' ', '_____' * (len(h) + 1)+'____')
    for elem in row:
        print(' |', elem, end='')
    print(' |')
print(' ', '_____'*(len(h)+1) +'____')


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
    	for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
