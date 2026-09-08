def power(base,exponential):
    if exponential == 0 :
        return 1
    return base*power(base,exponential-1)
pow=power(2,5)
print("2**5 =",pow)