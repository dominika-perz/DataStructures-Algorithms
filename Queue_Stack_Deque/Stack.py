from array import array


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            IndexError("pop from empty stack")

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
