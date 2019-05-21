
"""
INSERTION SORT

--> Not really efficient
--> Useful for small datasets
--> Big O --> O(n²) --> nested loops
"""

"""NOT WORKING"""
def insertion_sort(list):
    result = list

    for i in range(1, len(result)):
        # Reference to compare
        key_pointer = result[i]
        j = i-1
        while(j>=0 and key_pointer < result[j]):
            result[j+1] = result[j]
            j -= 1
        result[j+1] = key_pointer

    return result


