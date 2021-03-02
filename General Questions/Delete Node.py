"""
Given a singly linked list and a position, delete a linked list node at the given position.

Example:  

Input: position = 1, Linked List = 8->2->3->1->7
Output: Linked List =  8->3->1->7

Input: position = 0, Linked List = 8->2->3->1->7
Output: Linked List = 2->3->1->7
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
        while temp is not None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_pos(self, position):
        count = 0
        temp = self.head

        if temp is not None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return
        count = 1
        prev = temp
        temp = temp.next
        while temp is not None:
            if count == position:
                prev.next = temp.next
            prev = temp
            temp = temp.next
            count += 1

llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printList()

llist.delete_pos(3)
llist.printList()