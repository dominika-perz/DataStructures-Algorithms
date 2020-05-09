class SingleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def linked_list_reversal(head):
    node = head
    prev = None

    while node is not None:
        new_node = SingleLinkedListNode(node.data)
        new_node.next = prev
        node = node.next
        prev = new_node

    return new_node


def linked_list_reversal(head):
    node = head
    prev = None

    while node is not None:
        new_node = SingleLinkedListNode(node.data)
        new_node.next = prev
        node = node.next
        prev = new_node

    return new_node


def nth_to_last(n, head):
    node = head
    nth_node = None
    i = 0

    while node is not None:
        if i == n - 1:
            nth_node = head
        elif i >= n:
            nth_node = nth_node.next
        node = node.next
        i += 1

    return nth_node


def cycle_check(head):
    node_slow = head
    node_fast = head

    while node_slow is not None and node_fast.next is not None:
        node_slow = node_slow.next
        node_fast = node_fast.next.next
        if node_fast == node_slow:
            return True

    return False
