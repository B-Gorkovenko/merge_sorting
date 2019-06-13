import unittest
import mergesort as method
import random

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
        items4 = [7, 5, 3, 7, 5,
                  7, 5, 3, 7]
        method.mergeSort(items4)
        assert items4 == [3, 3, 5, 5, 5,
                          7, 7, 7, 7]

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = []
        for x in range(0, 20):
            items1.append(random.randint(1, 10))
        print(items1)
        sorted_items1 = method.mergeSort(items1)  # Create a copy of list in sorted order
        sorted(items1)  # Call mutative sort function to sort list items in place
        print(items1)
        print("AAAA")
        print(sorted_items1)
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = []
        for x in range(0, 50):
            items2.append(random.randint(1, 20))
        sorted_items2 = method.mergeSort(items2)  # Copy
        sorted(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = []
        for x in range(0, 100):
            items3.append(random.randint(1, 30))
        sorted_items3 = method.mergeSort(items3)  # Copy
        sorted(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = []
        for x in range(0, 10):
            items1.append(random.randint(1, 20))
        sorted_items1 = method.mergeSort(items1)  # Create a copy of list in sorted order
        sorted(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = []
        for x in range(0, 20):
            items2.append(random.randint(1, 50))
        sorted_items2 = method.mergeSort(items2)  # Copy
        sorted(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = []
        for x in range(0, 30):
            items3.append(random.randint(1, 100))
        sorted_items3 = method.mergeSort(items3)  # Copy
        sorted(items3)  # Mutate
        assert items3 == sorted_items3

unittest.main()
items1 = [25, 14, 26]
