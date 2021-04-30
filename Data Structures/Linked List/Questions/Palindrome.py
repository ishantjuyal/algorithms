"""
Function to check if a singly linked list is palindrome
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
    
    def palindrome(self):
        check_list = []
        temp = self.head
        while temp:
            check_list.append(temp.data)
            temp = temp.next
        return(check_list == check_list[::-1])
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")


if __name__ == '__main__':
    l = LinkedList()
    s = [ 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'g' ]
     
    for i in range(len(s)):
        l.push(s[i])
    
    l.printList()
    print("Is the Linked List palindrome?")
    print(l.palindrome())