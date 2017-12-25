def is_prime(n):
    if n == 1:
        return True
    else:
        for i in range(2,n+1):
            if i == n and n % i == 0:
                return True
            elif i != n and n % i ==0:
                return False

def n_first_prime():

    count = 1
    while count <= 23:
        if is_prime(count) == True:
            print(count)
            count +=1


        else:
            count +=1


n_first_prime()
