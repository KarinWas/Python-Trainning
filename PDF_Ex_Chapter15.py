import unittest
from PDF_Ex_Chapter12 import factorial, quicksort

class TestFactorial(unittest.TestCase):
    def test_five(self):
        self.assertEqual(factorial(5), 120)
    
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

class TestQuickSort(unittest.TestCase):
    def test_sorted_list(self):
        list = [1, 2, 3, 4 ,5, 6, 7, 8]
        self.assertEqual(quicksort(list), list)

    def test_not_sorted_list(self):
        list = [13, 5, 88, 10, 12, 1, 4, 9]
        sortedList = [1, 4, 5, 9, 10, 12, 13, 88]
        self.assertEqual(quicksort(list), sortedList)

if __name__ == '__main__':
    unittest.main()