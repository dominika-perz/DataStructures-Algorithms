from array import array


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            IndexError("dequeue from empty queue")

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
