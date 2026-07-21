def list_sum(numbers):
    if len(numbers) == 0:        # base case
        return 0
    else:
        return numbers[0] + list_sum(numbers[1:])   # recursive case

print(list_sum([3, 5, 2]))   # 10