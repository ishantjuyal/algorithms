class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        print()

    # Add a node to the front:
    # The new node is always added before the head of the given Linked List. 
    # And newly added node becomes the new head of the Linked List.

    def push(self, new_data):
        # Make a new node with new data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Make the head to point to New Node
        self.head = new_node
    
    # Add a node after a given node:

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous note must be in Linked List")
            return
        
        # Create a new node with new data
        new_node = Node(new_data)

        # Make next of previous node as next of new node
        new_node.next = prev_node.next

        # make new node as next of previous node
        prev_node.next = new_node
    
    # Add a node at the end
    # The new node is always added after the last node of the given Linked List.

    def append(self, new_data):
        # Make a new node for new data
        new_node = Node(new_data)

        # if linked list is empty
        if self.head is None:
            # Make the new node as head
            self.head = new_node
            return
        
        # Else, traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        
        # Change the next of last node
        last.next = new_node

if __name__=='__main__':

    llist = LinkedList()

    # Push node at end of list
    llist.append(6)
    llist.printList()

    # Insert at the start
    llist.push(7)
    llist.printList()

    llist.push(1)
    llist.append(4)
    llist.printList()

    llist.insertAfter(llist.head.next, 8)
    llist.printList()