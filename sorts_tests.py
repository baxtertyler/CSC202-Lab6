import unittest
from sorts import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection(self):
        # best
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        comps1 = selection_sort(list1)
        self.assertEqual(comps1, 45)
        self.assertEqual(list1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # average
        list2 = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]
        comps2 = selection_sort(list2)
        self.assertEqual(comps2, 45)
        self.assertEqual(list2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # worst
        list3 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        comps3 = selection_sort(list3)
        self.assertEqual(comps3, 45)
        self.assertEqual(list3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_insertion(self):
        # best
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        comps1 = insertion_sort(list1)
        self.assertEqual(comps1, 9)
        self.assertEqual(list1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # worst
        list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        comps2 = insertion_sort(list2)
        self.assertEqual(comps2, 45)
        self.assertEqual(list2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # average
        list3 = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]
        comps3 = insertion_sort(list3)
        self.assertEqual(comps3, 19)
        self.assertEqual(list3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




if __name__ == '__main__':
    unittest.main()
