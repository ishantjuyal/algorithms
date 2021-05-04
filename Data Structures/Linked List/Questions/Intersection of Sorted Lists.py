"""
Intersection of two Sorted Linked Lists

Given two lists sorted in increasing order, create and return a new list representing the 
intersection of the two lists. 

The new list should be made with its own memory — the original lists should not be changed.

(Intersection as in sets, elements present in both lists)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
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

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")
    
def intersection(list_1,list_2):
    head_2 = list_2.head
    head_1 = list_1.head
    new_list = LinkedList()

    while (head_1 != None) and (head_2 != None):
        if head_1.data == head_2.data:
            new_list.append(head_1.data)
            head_1 = head_1.next
            head_2 = head_2.next
        elif head_1.data > head_2.data:
            head_2 = head_2.next
        elif head_1.data < head_2.data:
            head_1 = head_1.next
        else:
            pass
    new_list.printList()
    
if __name__=='__main__':
    a = LinkedList()
    b = LinkedList()

    a.push(5)
    a.push(4)
    a.push(3)
    a.push(1)

    b.push(4)
    b.push(3)
    b.push(2)
    b.push(1)
    
    a.printList()
    b.printList()
    
    intersection(a,b)