def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
    	for j in range(i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
tmp = [8, 9, 11, 666, 3, 0, 25, 1, 7, 4, 33, 2, 105, 6, 555]
print()
bubbleSort(tmp)
for elem in tmp:
    print(elem, end=' ')
print()