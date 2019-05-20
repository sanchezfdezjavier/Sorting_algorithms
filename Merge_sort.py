import Helpers as hlp

"""
MERGE-SORT algorithm (Divide and conquer)
Big O time complexity --> O(n*log(n))
Big O memory complexity --> O(n)
Great for big datasets
"""

# Where the real sort happens
def merge(left, right):
    result = []
    i = j = 0

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Recursive calls to the sort of each half. Here happens de divide an conquer(splitting the list)
def merge_sort(list):
    if (len(list) <= 1):
        return list
    else:
        middle = int(len(list) // 2)
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])

    return merge(left, right)
