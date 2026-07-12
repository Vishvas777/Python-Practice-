from typing import List


def arrayRankTransform(arr: List[int]) -> List[int]:
    # Handle empty input
    if not arr:
        return []

    # Map each unique number to its rank (1-based)
    num_to_rank = {}
    sorted_arr = sorted(arr)
    rank = 1
    for i in range(len(sorted_arr)):
        if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
            rank += 1
        num_to_rank[sorted_arr[i]] = rank

    # Replace each element with its rank
    return [num_to_rank[x] for x in arr]