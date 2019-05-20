import random as rnd
import time

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

    return (str(toc - tic)+ " seconds")
