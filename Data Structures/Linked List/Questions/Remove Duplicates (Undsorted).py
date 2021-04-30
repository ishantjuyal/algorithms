"""
Remove duplicates from an unsorted linked list
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
        check_list = []
        temp = self.head
        while temp.next is not None:
            if temp.data not in check_list:
                check_list.append(temp.data)
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
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
    llist.push(16)
    llist.push(11)
    llist.push(12)
    llist.push(19)
    llist.push(13)
    llist.push(16)
    llist.push(11)
    llist.push(12)

    llist.printList()
    llist.remove_duplicate()
    llist.printList()
    