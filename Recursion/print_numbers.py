def print_numbers(n):
    if n==0 :
        return
    print(n)
    print_numbers(n-1)
print_numbers(5)