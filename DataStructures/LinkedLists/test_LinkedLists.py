import unittest
from DataStructures.LinkedLists.SingleLinkedListNode import *
from DataStructures.LinkedLists.DoubleLinkedListNode import *


class TestInterviewProblems(unittest.TestCase):
    def test_linked_list_reversal(self):
        # Create a list of 4 nodes
        head = SingleLinkedListNode(1)
        b = SingleLinkedListNode(2)
        head.next = b
        c = SingleLinkedListNode(3)
        b.next = c
        d = SingleLinkedListNode(4)
        c.next = d

        reversed_head = linked_list_reversal(head)
        node = reversed_head
        for i in range(4, 0, -1):
            self.assertEqual(node.data, i)
            if node.next is not None:
                node = node.next

    def test_nth_to_last(self):
        head = SingleLinkedListNode(1)
        b = SingleLinkedListNode(2)
        head.next = b
        c = SingleLinkedListNode(3)
        b.next = c
        d = SingleLinkedListNode(4)
        c.next = d
        e = SingleLinkedListNode(5)
        d.next = e
        self.assertEqual(nth_to_last(2, head), d)

    def test_cycle_check(self):
        head = SingleLinkedListNode(1)
        b = SingleLinkedListNode(2)
        head.next = b
        c = SingleLinkedListNode(3)
        b.next = c
        d = SingleLinkedListNode(4)
        c.next = d
        e = SingleLinkedListNode(5)
        d.next = e
        self.assertFalse(cycle_check(head))

        e.next = c
        self.assertTrue(cycle_check(head))





if __name__ == '__main__':
    unittest.main()
