import Helpers as hlp
import  Merge_sort as mrg

test_case1 = hlp.random_list(10000, -10, 30)
print("Unsorted random list:\n{}\n\n".format(test_case1))

print("Sorted list:\n{}\n".format(mrg.merge_sort(test_case1)))
print("The megesort takes: {} seconds to sort".format(hlp.crono(mrg.merge_sort(test_case1))))
