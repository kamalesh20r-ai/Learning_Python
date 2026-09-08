def fibonacci(n):
    if n==0 :
        return 0
    if n==1 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number to find fibonnaci series :"))
f=fibonacci(n)
print("The Fibonacci Series for",n,"is",f)