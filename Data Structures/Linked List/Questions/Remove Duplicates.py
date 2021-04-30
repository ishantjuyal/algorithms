"""
Remove duplicates from a sorted linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def remove_duplicate(self):
        temp = self.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(13)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(11)

    llist.printList()
    llist.remove_duplicate()
    llist.printList()
    