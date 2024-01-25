# Make a node => (data, next)
# the first node looks like ('Atari', None)
# "Atari 400" => ('Atari 400', None)
# "Vic 20" => ('Vic 20', None)
# the linked list is a series of nodes, my_fav_computers = atari_node => cbm_node => None


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = None  # Fix: Assign None to new_node.next
            self.head = new_node

atari_node = Node('Atari 400')
cbm_node = Node('Vic 20')

my_fav_computers = linked_list()

my_fav_computers.add_node(atari_node)
print(my_fav_computers)