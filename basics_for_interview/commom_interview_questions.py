# How to swap two variavles in python?
def swapNumbers():
    x: int = 5
    y: int = 10

    #first method 
    temp = x
    x = y
    y = temp

    #second method
    x,y = y,x

    print(x, y)

#How to check if the number is a prime number?
def checkIfPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

#How to fund out the factorial of a number?
def factorial(num):
    factorial = 1
    if num < 0:
        return "its not a factorial"
    elif num == 0:
        return "the factorial of 0 is 1"
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return f"factory of {num} is {factorial}"
    

#how to generate random numbers?
def randonNumber():
    import random
    num = random.random()
    return num

#print the firt ten numbers of Fibonacci Series
def fibonacci(num):
    a, b = 0, 1
    if num < 1:
        print("null")       
    elif num == 1:
        print(a)
    elif num == 2:
        print(b)
    elif num > 2:
        print(a)
        print(b)
        for _ in range(num-2):
            c = a + b
            a, b = b, c
            print(c)
        
