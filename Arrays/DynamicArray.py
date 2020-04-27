import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self._capacity = 1
        self.array = self._make_new_array()

    def __setitem__(self, key, value):
        if 0 <= key < self.n:
            self.array[key] = value
        else:
            return IndexError('Key out of bounds!')

    def __getitem__(self, key):
        if 0 <= key < self.n:
            return self.array[key]
        else:
            return IndexError('Key out of bounds!')

    def append(self, item):
        if self.n == self._capacity:
            self._resize()

        self.array[self.n] = item
        self.n += 1

    def __len__(self):
        return self.n

    def _resize(self):
        self._capacity += self._capacity
        new_array = self._make_new_array()
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array

    def _make_new_array(self):
        return (self._capacity * ctypes.py_object)()
