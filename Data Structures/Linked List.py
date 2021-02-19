# A class for Node
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data to the node
        self.next = None # Initialize next pointer as null

# A class for Linked List
class LinkedList:
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

# A simple Linked List with 3 Nodes

if __name__ == '__main__':

    # An empty Linked List
    l_list = LinkedList()

    l_list.head = Node(1) # The first node is now the head of the Linked List
    second = Node(2) 
    third = Node(3)

    # second and third are nodes which are not linked with the linked list for now

    l_list.head.next = second # The .next of the first node of the linked list is now referring to the second note

    second.next = third # The .next of the second node of the linked list is now referring to the third node

    l_list.print()