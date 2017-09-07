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
b = random_array(10) #manipulation with zeros and ones
for i in range(len(b)):
    for j in range(len(b[i])):
        if j == i: #diagonal elements change to zeros
            b[i][j] = 0
        if b[i][j] > 0 and b[i][j] % 2 == 0: #pair elemelts to ones
            b[i][j] = 1
        elif b[i][j] % 2 == 1: #odd elements to zeros
            b[i][j] = 0
print_array(b)
print()

c = random_array(10)# array for turning array c to 90 degree
h = random_array(10) #temp array for turning array c to 90 degree
print_array(c)
print()

for i in range(len(c)):
    for j in range(len(c[i])):
         h[i][j] = c[len(c)-1-j][i]

for i in range(len(c)):
    for j in range(len(c[i])):
         c[i][j] = h[i][j]


print_array(c)
print()

tmp =[]  #raw with maximum summa
sum =0
count = 0
for i in range(len(c)):
    for j in range(len(c[i])):
        if count < len(c):
            sum += c[i][j]
            count +=1
        else:
            tmp =tmp +[sum]
            count = 1
            sum = 0
            sum += c[i][j]

tmp =tmp +[sum]

ind = tmp.index(max(tmp))


for j in range(len(c)):      #the sting with maximum summa
    print(c[ind][j], end=' ')
print()
