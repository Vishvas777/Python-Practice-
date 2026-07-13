# Function to calculate the sum of elements in an array
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Driver code
if __name__ == "__main__":
    # Example array
    arr = [1, 2, 3, 4, 5]
    
    # Print the result
    print("Array:", arr)
    print("Sum of array:", sum_array(arr))
