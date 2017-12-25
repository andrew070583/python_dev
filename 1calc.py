def plus(a,b):
    res = a + b
    return res

def minus(a,b):
    res = a - b
    return res

def multiplication(a,b):
    res = a * b
    return res

def division(a,b):
    if b < 0 or b > 0:
        res = a / b
    else:
        res = print('division by 0 is not possible ')

    return res

def to_degree(a, b):
    res = a ** b
    return res

def sin(number1,number2):
    res = number1 / ((number1 ** 2 + number2 ** 2) ** 0.5)
    return res
def cos(number1,number2):
    res = number2 / ((number1 ** 2 + number2 ** 2) ** 0.5)
    return res
def calculation():
    while  True:
        response = input(' if you want to continue type y/n: ')
        if response == 'y':
            number1 = int(input('number1:'))
            number2 = int(input('number2:'))
            operation = input('operation')
            if operation == '+':
                print(plus(number1, number2))
            elif operation == '-':
                print(minus(number1, number2))
            elif operation == '*':
                print(multiplication(number1, number2))
            elif operation == '/':
                print(division(number1, number2))
            elif operation == '**':
                print(to_degree(number1, number2))
            elif operation == 'sin':
                print(sin(number1, number2))
            elif operation == 'cos':
                print(cos(number1, number2))
        else:
            break



calculation()