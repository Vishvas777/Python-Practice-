def second_largest(arr):
    if arr[0] > arr[1]:
        biggest, second = arr[0], arr[1]
    else:
        biggest, second = arr[1], arr[0]

    for num in arr[2:]:
        if num > biggest:
            second = biggest
            biggest = num
        elif num > second and num != biggest:
            second = num

    return second


print(second_largest([15, 6, 15, 3, 20]))   # 20... wait, check this