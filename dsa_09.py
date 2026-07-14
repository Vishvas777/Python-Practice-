def is_sorted(arr):
    # Loop through the array and check adjacent elements
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 1, 4, 2]

print("Array:", arr1, "-> Sorted?", is_sorted(arr1))  # True
print("Array:", arr2, "-> Sorted?", is_sorted(arr2))  # False
