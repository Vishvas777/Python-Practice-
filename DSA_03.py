
def find_max(arr):
    """
    Returns the largest element in arr.
    Time Complexity: O(n) -- single pass through the list.
    """
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def has_duplicate(arr):
    """
    Returns True if arr contains any duplicate value.
    Time Complexity: O(n^2) -- nested loop compares every pair.
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False


def find_min(arr):
    """
    Practice Problem 1: Returns the smallest element in arr
    without using Python's built-in min().
    Time Complexity: O(n) -- single pass through the list.
    """
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


def remove_duplicates(arr):
    """
    Practice Problem 2: Removes duplicate values while keeping
    the order of first appearance.
    Time Complexity: O(n) -- one pass, set lookups are O(1) average.
    """
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def mystery(arr):
    """
    Practice Problem 3: What's the time complexity?
    Answer: O(n^2) -- for every element in arr (n), we loop through
    arr again (n), so total operations = n * n.
    """
    total = 0
    for num in arr:
        for other in arr:
            total += num * other
    return total


def array_operations_demo():
    """
    Demonstrates core array (list) operations and their complexity.
    """
    arr = [10, 20, 30, 40, 50]

    print("Access arr[2] -> O(1):", arr[2])
    print("Search 30 in arr -> O(n):", 30 in arr)

    arr.append(60)  # O(1) amortized
    print("After append(60) -> O(1) amortized:", arr)

    arr.insert(1, 15)  # O(n), shifts everything after index 1
    print("After insert(1, 15) -> O(n):", arr)

    arr.remove(15)  # O(n), find + shift
    print("After remove(15) -> O(n):", arr)

    del arr[0]  # O(n) worst case
    print("After del arr[0] -> O(n):", arr)


if __name__ == "__main__":
    sample = [3, 1, 4, 1, 5, 9, 2, 6]

    print("Sample array:", sample)
    print("Max:", find_max(sample))
    print("Min:", find_min(sample))
    print("Has duplicate:", has_duplicate(sample))
    print("Without duplicates:", remove_duplicates(sample))
    print()
    array_operations_demo()