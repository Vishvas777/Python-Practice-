def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# Trace it against the same example we hand-solved
sample = [3, 8, 4, 1, 6]
print(count_evens(sample))   # 3