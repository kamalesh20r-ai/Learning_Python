def find_max(numbers):
    if len(numbers)==1:
        return numbers[0]
    rem_max=find_max(numbers[1:])
    if numbers[0] > rem_max:
        return numbers[0]
    return rem_max
maximum=find_max([45, 12, 89, 34, 67])
print("Maximum Number in the given List is",maximum)