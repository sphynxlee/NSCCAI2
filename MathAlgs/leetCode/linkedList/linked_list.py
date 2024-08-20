# Make a node => (data, next)
# the first node looks like ('Atari', None)
# "Atari 400" => ('Atari 400', None)
# "Vic 20" => ('Vic 20', None)
# the linked list is a series of nodes, my_fav_computers = atari_node => cbm_node => None

from typing import Optional

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Otherwise, traverse to the end of the list and add the new node there
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return " => ".join(result)

my_fav_computers = LinkedList()

my_fav_computers.add_node('Atari 400')
my_fav_computers.add_node('Vic 20')

print(my_fav_computers)
