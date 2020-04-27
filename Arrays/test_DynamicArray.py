from unittest import TestCase
from Arrays.DynamicArray import DynamicArray


class TestInit(TestCase):
    def test_empty_init(self):
        new_array = DynamicArray()
        self.assertIsInstance(new_array, DynamicArray)

    def test_empty_init_n(self):
        new_array = DynamicArray()
        self.assertEqual(new_array.n, 0)

    def test_empty_init_capacity(self):
        new_array = DynamicArray()
        self.assertEqual(new_array._capacity, 1)


class TestLen(TestCase):
    def test_init_len(self):
        new_array = DynamicArray()
        self.assertEqual(len(new_array), 0)


class TestBasicAssignment(TestCase):
    def test_append(self):
        new_array = DynamicArray()
        new_array.append(1)
        self.assertEqual(new_array.array[0], 1)

    def test_append_len(self):
        new_array = DynamicArray()
        for i in range(10):
            new_array.append(i*3)
            self.assertEqual(len(new_array), i+1)

    def test_append_capacity(self):
        new_array = DynamicArray()
        cap = [1, 2, 4, 4, 8, 8, 8, 8, 16, 16]
        for i in range(10):
            new_array.append(i*3)
            self.assertEqual(len(new_array), i+1)


class TestGetItem(TestCase):
    def test_append(self):
        new_array = DynamicArray()
        for i in range(10):
            new_array.append(i*3)
        for i in range(10):
            self.assertEqual(new_array[i], i*3)