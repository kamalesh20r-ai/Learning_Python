def factorial(n):
    if n == 1 :
        return 1
    return n*factorial(n-1)
fact=factorial(5)
print("Factorial of first five numbers is ",fact)