import ctypes


class MinHeap:
    """
    >>> heap = MinHeap()
    >>> heap.isEmpty()
    True
    >>> heap.insert(2)
    >>> heap.isEmpty()
    False
    >>> heap.insert(6)
    >>> heap.insert(4)
    >>> heap.insert(1)
    >>> heap.insert(9)
    >>> heap.insert(3)
    >>> heap.insert(5)
    >>> heap.insert(1)
    This item is already in the heap.
    >>> print(heap)
    [1, 2, 3, 6, 9, 4, 5]
    >>> len(heap)
    7
    >>> heap.remove(6)
    >>> print(heap)
    [1, 2, 3, 5, 9, 4]
    >>> heap.remove(6)
    Item not found
    >>> heap.remove(1)
    >>> print(heap)
    [2, 4, 3, 5, 9]
    >>> len(heap)
    5
    >>> heap.remove(3)
    >>> print(heap)
    [2, 4, 9, 5]
    """

    def __init__(self):
        self._size = 0
        self._capacity = 8
        self._heap = self._make_new_array()

    def __len__(self):
        return self._size

    def __str__(self):
        return str([self._heap[index] for index in range(self._size)])

    def isEmpty(self):
        return self._size == 0

    def contains(self, item):
        return self._find(item) != -1

    def poll(self):
        item = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._heap[self._size - 1] = None
        self._size -= 1
        self._sink(0)
        return item

    def remove(self, item):
        index = self._find(item)
        if index == -1:
            print('Item not found')
            return
        elif index == self._size - 1:
            self._heap[index] = None
            self._size -= 1
            return
        self._swap(index, self._size - 1)
        self._heap[self._size - 1] = None
        self._size -= 1

        self._swim(index)
        self._sink(index)

    def insert(self, item):
        if self.contains(item):
            print('This item is already in the heap.')
            return
        if self._size == self._capacity:
            self._doubleCapacity()
        index = self._size
        self._heap[index] = item
        self._size += 1
        self._swim(index)

    def _doubleCapacity(self):
        self._capacity *= 2
        new_heap = self._make_new_array()
        for index in range(self._size):
            new_heap[index] = self._heap[index]
        self._heap = new_heap

    def _find(self, item):
        for index in range(self._size):
            if self._heap[index] == item:
                return index
        return -1

    def _swim(self, index):
        if index == 0:
            return
        parent = self._parentOf(index)
        if self._heap[parent] < self._heap[index]:
            return

        self._swap(parent, index)
        self._swim(parent)

    def _sink(self, index):
        left, right = self._childrenOf(index)
        if left == -1:
            return
        elif right == -1:
            if self._heap[left] > self._heap[index]:
                return
            else:
                self._swap(index, left)
                self._sink(left)
        elif (self._heap[left] < self._heap[index]) | (self._heap[right] < self._heap[index]):
            if self._heap[left] < self._heap[right]:
                self._swap(index, left)
                self._sink(left)
            else:
                self._swap(index, right)
                self._sink(right)

    def _swap(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def _parentOf(self, index):
        return (index - 1) // 2

    def _childrenOf(self, index):
        left = 2 * index + 1
        if left >= self._size:
            left = -1
        right = 2 * index + 2
        if right >= self._size:
            right = -1

        return left, right

    def _make_new_array(self):
        return (self._capacity * ctypes.py_object)()
