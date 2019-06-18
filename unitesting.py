import unittest
import random
from mergesort import mergeSort


class IntegerSortTest(unittest.TestCase):
    def test_sort_on_empty_list(self):
        alist = []
        mergeSort(alist)
        self.assertEqual(alist, [])  # List should not be changed

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        mergeSort(items1)
        self.assertEqual(items1, [3, 3])  # List should not be changed
        items2 = [3, 5, 3]
        mergeSort(items2)
        self.assertEqual(items2, [3, 3, 5])  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        mergeSort(items3)
        self.assertEqual(items3, [3, 3, 5, 5, 5])
        items4 = [7, 5, 3, 7, 5,
                  7, 5, 3, 7]
        mergeSort(items4)
        self.assertEqual(items4, [3, 3, 5, 5, 5,
                                  7, 7, 7, 7])

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = []
        for x in range(0, 10):
            items1.append(random.randint(1, 20))
        sorted_items1 = mergeSort(items1)  # Creating a copy of list
        sorted(items1)  # Sorting list items in place
        self.assertEqual(items1, sorted_items1)

        # Generate list of 20 random integers from range [1...50]
        items2 = []
        for x in range(0, 20):
            items2.append(random.randint(1, 50))
        sorted_items2 = mergeSort(items2)  # Copy
        sorted(items2)  # Mutate
        self.assertEqual(items2, sorted_items2)

        # Generate list of 30 random integers from range [1...100]
        items3 = []
        for x in range(0, 30):
            items3.append(random.randint(1, 100))
        sorted_items3 = mergeSort(items3)  # Copy
        sorted(items3)  # Mutate
        self.assertEqual(items3, sorted_items3)


if __name__ == "__main__":
    unittest.main()
