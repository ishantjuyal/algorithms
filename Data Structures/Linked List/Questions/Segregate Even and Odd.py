"""
Segregate even and odd nodes in a Linked List

Given a Linked List of integers, write a function to modify the linked list such that all 
even numbers appear before all the odd numbers in the modified linked list. 
Also, keep the order of even and odd numbers same.

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

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")
    
    def segregate(self):
        odd_head = None
        odd_end = None
        even_head = None
        even_end = None

        temp = self.head
        while temp:
            if temp.data % 2 != 0:
                if odd_head == None:
                    odd_head = temp
                    odd_end = odd_head
                else:
                    odd_end.next = temp
                    odd_end = odd_end.next
            else:
                if even_head == None:
                    even_head = temp
                    even_end = even_head
                else:
                    even_end.next = temp
                    even_end = even_end.next
            temp = temp.next
        
        return(even_head, even_end, odd_head, odd_end)


if __name__ == '__main__':
    llist = LinkedList()
      
    # swap the 2 nodes
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.printList()
    
    even_head, even_end, odd_head, odd_end = llist.segregate()

    new_list = LinkedList()

    even_end.next = odd_head
    odd_end.next = None
    
    new_list.head = even_head
    new_list.printList()