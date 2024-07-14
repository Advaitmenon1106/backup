def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Splitting the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive call on each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merging the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    # Merge the two halves while they both have elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Add remaining elements from left half
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    
    # Add remaining elements from right half
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    
    return result

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)