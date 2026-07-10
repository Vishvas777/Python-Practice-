# O(n) - one loop, time grows linearly with input size
def find_max(arr):
    max_val = arr[0]
    for num in arr:        # runs n times
        if num > max_val:
            max_val = num
    return max_val

# O(n^2) - nested loop, time grows quadratically
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):   # for EVERY i, loop through all n again
            if i != j and arr[i] == arr[j]:
                return True
    return False