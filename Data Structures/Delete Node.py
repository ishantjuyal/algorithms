"""
Iterative Method:
To delete a node from the linked list, we need to do the following steps. 
1) Find the previous node of the node to be deleted. 
2) Change the next of the previous node. 
3) Free memory for the node to be deleted.
"""

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

    def push(self, new_data):
        # Make a new node with new data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Make the head to point to New Node
        self.head = new_node
    
    # Given a reference to the head of a list and a key, 
    # delete the first occurence of key in linked list
    def deleteNode(self, key):

        # Store head node 
        temp_head = self.head

        # If head node itself holds the key to be deleted
        if temp_head is not None:
            if temp_head.data == key:
                self.head = temp_head.next
                temp_head = None
                return
        
        # Search for the key to be deleted in the Linked List
        # Keep Track of the previous node as we need to change .next for that
        while temp_head is not None:
            if temp_head.data == key:
                break
            prev = temp_head
            temp_head = temp_head.next
        
        # If key was not present in Linked List
        if temp_head == None:
            return
        
        # Unlink the node from Linked List
        prev.next = temp_head.next

llist = LinkedList()
llist.push(5)
llist.push(9)
llist.push(6)
llist.push(2)
llist.push(1)

print("List before deleting:")
llist.printList()

print("\nList after deleting:")
llist.deleteNode(5)
llist.printList()

print("\nList after deleting:")
llist.deleteNode(6)
llist.printList()