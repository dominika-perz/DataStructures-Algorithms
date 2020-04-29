from Queue_Stack_Deque.Stack import Stack


def parentheses_check(string):
    parentheses = Stack()
    pair = {'{': '}', '[': ']', '(': ')'}

    for char in string:
        if char in pair.keys():
            parentheses.push(char)
        elif char in pair.values():
            if not parentheses.isEmpty() and char == pair[parentheses.peek()]:
                parentheses.pop()
            else:
                return False

    return parentheses.isEmpty()


class TwoStackQueue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, item):
        if self.enqueue_stack.isEmpty():
            while not self.dequeue_stack.isEmpty():
                self.enqueue_stack.push(self.dequeue_stack.pop())
        self.enqueue_stack.push(item)

    def dequeue(self):
        if self.dequeue_stack.isEmpty():
            if self.enqueue_stack.isEmpty():
                IndexError
            while not self.enqueue_stack.isEmpty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self):
        if self.dequeue_stack.isEmpty():
            if self.enqueue_stack.isEmpty():
                IndexError
            while not self.enqueue_stack.isEmpty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.peek()

    def isEmpty(self):
        return self.enqueue_stack.isEmpty() and self.dequeue_stack.isEmpty()

    def __len__(self):
        return max(len(self.enqueue_stack), len(self.dequeue_stack))
