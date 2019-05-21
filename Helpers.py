import random as rnd
import time
from Javis_algorithms import Merge_sort as mrg
from Data_Structures import Binary_tree as bnt

""" SOME SILLY FUNCTIONS TO TEST THE ALGORITHMS PERFORMANCE"""

# Random list generator function
def random_list(leng, lower_bound, upper_bound):
    list = []
    for i in range(leng):
        list.append(rnd.randint(lower_bound, upper_bound))

    return list

# Times run time of a given function
def crono(random_function):
    tic = time.time()
    random_function
    toc = time.time()

    return (toc - tic)

# Percentage performance comparaison
def time_ratio(algo1, algo2):
    ratio = crono(algo2)/crono(algo1) * 100
    return (str(ratio) + '%')


def random_tree_gerator(numNodes, lowerBound, upperBound):
    random_data = random_list(numNodes, lowerBound, upperBound)
    sorted_data = mrg.merge_sort(random_data)

    # Construction of our binary tree
    middle_idx = len(sorted_data) // 2
    root = bnt.Node(sorted_data.pop(middle_idx))

    for element in sorted_data:
        root.insert(element)

    return root

def print_tree(tree):
    if tree.left:
        tree.left.print_tree()
    print(tree.data),
    if tree.right:
        tree.right.print_tree()
