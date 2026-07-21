def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements

    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None


# Example usage
arr1 = [10, 20, 4, 45, 99]
arr2 = [5, 5, 5]  # all elements same
arr3 = [7]        # single element

print("Second largest in arr1:", second_largest(arr1))  # 45
print("Second largest in arr2:", second_largest(arr2))  # None
print("Second largest in arr3:", second_largest(arr3))  # None
