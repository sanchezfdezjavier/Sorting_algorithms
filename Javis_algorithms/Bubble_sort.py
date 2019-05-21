import Helpers as hlp

# Never use it please, what a shit!
def bubble_sort(list):
    result = list
    i, j = 0, 1
    if len(list) <= 1:
        return list
    else:
        while(j == len(list) -1):
            if list[i] > list[j]:
                aux = list[i]
                list[i] = list[j]
                list[j] = aux
                i += 1
                j += 1
            else:
                i += 1
                j += 1
    return result

