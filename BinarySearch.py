def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if target is not found

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 5
index = binary_search(arr, target)
if index != -1:
    print(f"The target value {target} is found at index {index}.")
else:
    print("The target value is not present in the array.")
