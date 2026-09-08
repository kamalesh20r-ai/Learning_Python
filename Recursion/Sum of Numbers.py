def sum_numbers(n):
    if n == 1:
        return 1
    return n+sum_numbers(n-1)
s=sum_numbers(5)
print("Sum of First Five Numbers is ",s)