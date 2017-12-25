def is_prime(n):
    if n == 1:

        print(True)
    else:
        for i in range(2,n+1):
            if i == n and n % i == 0:
                print(True)
            elif i != n and n % i == 0:
                print(False)




is_prime(1)
