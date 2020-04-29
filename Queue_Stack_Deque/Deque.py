import array


class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(item, 0)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        try:
            return self.items.pop()
        except IndexError:
            IndexError("pop from empty deque")

    def removeRear(self):
        try:
            return self.items.pop(0)
        except IndexError:
            IndexError("pop from empty deque")

    def peekFront(self):
        return self.items[0]

    def peekRear(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
