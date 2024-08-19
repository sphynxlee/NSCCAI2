class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse current node's pointer
        prev = current            # Move prev to current node
        current = next_node       # Move to the next node

    return prev  # prev is the new head of the reversed list

# Example linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print reversed linked list: 4 -> 3 -> 2 -> 1 -> None
current = reversed_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
