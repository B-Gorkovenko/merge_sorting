import unittest
import mergesort as method


class IntegerSortTest(unittest.TestCase):
    def test_sort_on_empty_list(self):
        alist = []
        method.mergeSort(alist)
        self.assertEqual(alist, [])  # List should not be changed

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        method.mergeSort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        method.mergeSort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        method.mergeSort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        method.mergeSort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
if __name__ == '__main__':
    unittest.main()