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
    
    def intersection(self, list_2):
        head_1 = self.head
        head_2 = list_2.head
        ans = False
        collected = []

        while head_1.next and head_2.next:
            if head_1.data not in collected:
                collected.append(head_1.data)
                head_1 = head_1.next
            else:
                return(head_1)
                break
            if head_2.data not in collected:
                collected.append(head_2.data)
                head_2 = head_2.next
            else:
                return(head_2)
                break
            
            



if __name__ == '__main__':
    llist1 = LinkedList()
      
    # swap the 2 nodes
    llist1.push(6)
    llist1.push(5)
    llist1.push(4)
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)

    llist2 = LinkedList()
      
    # swap the 2 nodes
    llist2.push(6)
    llist2.push(5)
    llist2.push(4)
    llist2.push(9)
    llist2.push(5)

    print("First List:", end = " ")
    llist1.printList()
    print("Second List:", end = " ")
    llist2.printList()

    new_list = LinkedList()
    new_list.head = llist1.intersection(llist2)
    print("Intersection of Lists:", end = " ")
    new_list.printList()