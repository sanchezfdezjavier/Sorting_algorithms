import Helpers as hlp
from Javis_algorithms import Merge_sort as mrg

"""
BINARY TREE IMPLEMENTATION + RANDOM TREE GENERATOR

All the tree nodes have leaves, so the final nodes are full of None leaves
"""
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def random_tree_gerator(self, numNodes, lowerBound, upperBound):
        random_data = hlp.random_list(numNodes, lowerBound, upperBound)
        sorted_data = mrg.merge_sort(random_data)

        # Construction of our binary tree
        middle = sorted_data[len(sorted_data) // 2]
        root = Node(sorted_data.pop(middle))

        for element in sorted_data:
            root.insert(element)

        return root

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()








