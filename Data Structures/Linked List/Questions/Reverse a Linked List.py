"""
Reverse a linked list

Given pointer to the head node of a linked list, the task is to reverse the linked list.
We need to reverse the list by changing the links between nodes.
"""

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
    
    # Iterative Approach
    def reverse(self):
        temp = self.head
        prev = None
        next = None

        while temp:
            next = temp.next # Store next node in "next"
            temp.next = prev # Make the previous node as the next of the current node, hence reversing it
            prev = temp # Change the prev to set the reversal for next node
            temp = next # similar to temp = temp.next but doing with next node stored in "next"
        self.head = prev # Make the last node of the original list as head to reverse
    
    # Recursive Approach
    def reversal(self, head):
        if head is None or head.next is None:
            return head
        
        rest = self.reversal(head.next)
        
        head.next.next = head
        head.next = None

        return rest


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
    
    llist.head = llist.reversal(llist.head)
    llist.printList()