"""
Quicksort implementation
"""


def quicksort(arr):
    """
    Sorts an array using the quicksort algorithm.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        A new sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    Sorts an array in-place using the quicksort algorithm.
    
    Args:
        arr: List of comparable elements
        low: Starting index (default: 0)
        high: Ending index (default: len(arr) - 1)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partitions the array around a pivot element.
    
    Args:
        arr: List of comparable elements
        low: Starting index
        high: Ending index
        
    Returns:
        The index of the pivot after partitioning
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [1],
        [],
        [5, 5, 5, 5],
        [2, 1],
    ]
    
    print("Testing quicksort (simple version):")
    for test in test_cases:
        result = quicksort(test)
        print(f"  {test} -> {result}")
    
    print("\nTesting quicksort (in-place version):")
    for test in test_cases:
        arr = test.copy()
        quicksort_inplace(arr)
        print(f"  {test} -> {arr}")
