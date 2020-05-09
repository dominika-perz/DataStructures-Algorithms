import unittest
from DataStructures.Queue_Stack_Deque.Stack import Stack
from DataStructures.Queue_Stack_Deque.Queue import Queue
from DataStructures.Queue_Stack_Deque.InterviewProblems import parentheses_check, TwoStackQueue


class TestStack(unittest.TestCase):
    def test_is_instance(self):
        stack = Stack()
        self.assertIsInstance(stack, Stack)

    def test_push(self):
        stack = Stack()
        stack.push(3)
        self.assertEqual(stack.items[0], 3)
        self.assertEqual(len(stack), 1)
        for i in range(10):
            stack.push(i)
        self.assertEqual(stack.items[0], 3)
        self.assertEqual(stack.items[-1], 9)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        stack.push(3)
        self.assertFalse(stack.isEmpty())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)
        stack.pop()
        self.assertRaises(IndexError)

    def test_len(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
            self.assertEqual(len(stack), i+1)


class TestQueue(unittest.TestCase):
    def test_is_instance(self):
        queue = Queue()
        self.assertIsInstance(queue, Queue)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(3)
        self.assertEqual(queue.items[0], 3)
        self.assertEqual(len(queue), 1)
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(queue.items[0], 3)
        self.assertEqual(queue.items[-1], 9)

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())
        queue.enqueue(3)
        self.assertFalse(queue.isEmpty())

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        queue.dequeue()
        self.assertRaises(IndexError)

    def test_len(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
            self.assertEqual(len(queue), i+1)


class TestBalancedParenthesis(unittest.TestCase):
    def test_parentheses_check(self):
        self.assertEqual(parentheses_check('[](){([[[]]])}('), False)
        self.assertEqual(parentheses_check('[{{{(())}}}]((()))'), True)
        self.assertEqual(parentheses_check('[[[]])]'), False)
        self.assertEqual(parentheses_check('[[[]]]]'), False)


class TestTwoStackQueue(unittest.TestCase):
    def test_is_instance(self):
        queue = TwoStackQueue()
        self.assertIsInstance(queue, TwoStackQueue)

    def test_enqueue(self):
        queue = TwoStackQueue()
        queue.enqueue(3)
        self.assertEqual(len(queue), 1)
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(len(queue), 11)

    def test_is_empty(self):
        queue = TwoStackQueue()
        self.assertTrue(queue.isEmpty())
        queue.enqueue(3)
        self.assertFalse(queue.isEmpty())

    def test_dequeue(self):
        queue = TwoStackQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        queue.dequeue()
        self.assertRaises(IndexError)

    def test_len(self):
        queue = TwoStackQueue()
        for i in range(10):
            queue.enqueue(i)
            self.assertEqual(len(queue), i+1)


if __name__ == '__main__':
    unittest.main()
