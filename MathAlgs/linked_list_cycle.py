from typing import Optional

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['Node'] = None


def has_cycle(head):
    if not head or not head.next:
        return False

    current = head
    tail = head.next

    while tail and tail.next:
        if current == tail:
            return True

        current = current.next
        tail = tail.next.next

    return False

# Create a linked list with a cycle
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Creating a cycle
node5.next = node2

print(has_cycle(node1))


