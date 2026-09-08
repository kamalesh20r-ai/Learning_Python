def list_sum(numbers):
    if len(numbers)==0:
        return 0
    return numbers[0]+list_sum(numbers[1:])
num=list_sum([10, 20, 30, 40])
print("Sum of the Given List is ",num)