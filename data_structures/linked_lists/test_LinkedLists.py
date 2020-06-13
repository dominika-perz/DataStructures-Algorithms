import unittest
from data_structures.linked_lists.SingleLinkedListNode import *
from data_structures.linked_lists.DoubleLinkedListNode import *


class TestInterviewProblems(unittest.TestCase):
    def setUp(self):
        self.head = SingleLinkedListNode(1)
        b = SingleLinkedListNode(2)
        self.head.next = b
        c = SingleLinkedListNode(3)
        b.next = c
        d = SingleLinkedListNode(4)
        self.middle = d
        c.next = d
        e = SingleLinkedListNode(5)
        d.next = e

    def tearDown(self):
        pass

    def test_linked_list_reversal(self):
        reversed_head = linked_list_reversal(self.head)
        node = reversed_head
        for i in range(5, 0, -1):
            self.assertEqual(node.data, i)
            if node.next is not None:
                node = node.next

    def test_nth_to_last(self):
        self.assertEqual(nth_to_last(2, self.head), self.middle)

    def test_cycle_check(self):
        self.assertFalse(cycle_check(self.head))

        self.middle.next = self.head
        self.assertTrue(cycle_check(self.head))


if __name__ == '__main__':
    unittest.main()
