# List Utility Functions
# Common list operations and manipulations

def find_max(lst):
    """Find maximum element in list."""
    return max(lst) if lst else None

def find_min(lst):
    """Find minimum element in list."""
    return min(lst) if lst else None

def reverse_list(lst):
    """Reverse a list."""
    return lst[::-1]

def remove_duplicates(lst):
    """Remove duplicate elements from list."""
    return list(dict.fromkeys(lst))

def flatten_list(lst):
    """Flatten a nested list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def rotate_list(lst, k):
    """Rotate list by k positions."""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst

def find_common(lst1, lst2):
    """Find common elements between two lists."""
    return list(set(lst1) & set(lst2))

if __name__ == '__main__':
    # Test cases
    test_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Max: {find_max(test_list)}")  # 9
    print(f"Min: {find_min(test_list)}")  # 1
    print(f"Reversed: {reverse_list(test_list)}")
    print(f"No Duplicates: {remove_duplicates(test_list)}")
    print(f"Rotated by 2: {rotate_list(test_list, 2)}")
    print(f"Common in [1,2,3] and [2,3,4]: {find_common([1,2,3], [2,3,4])}")
