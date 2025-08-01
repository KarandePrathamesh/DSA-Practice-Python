# wap to create linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node   # append at lst pos
        else:
            self.head=new_node      # first pos if list is empty
        self.length+=1
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next

    def displaySum(self):
        temp = self.head
        sum = 0
        while temp:
            sum+=temp.data
            temp = temp.next
        print('sum of nodes is',sum)

    def displaySumOfAlternateNodes(self):
        temp = self.head
        sum = 0
        while temp:
            sum+=temp.data
            if temp.next != None:
                temp = temp.next.next
            else:
                temp = temp.next
        print('sum of alternate nodes is',sum)
    
    def print_reverse(self):
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        print('\nPrint reverse linked list :',arr[::-1])

    def remove_middle(self):
        mid = self.length//2
        temp = self.head
        i=0
        while i!=mid-1:
            temp=temp.next
            i+=1
        temp.next = temp.next.next

    def swap_pairs(self):
        temp=self.head
        while temp!=None and temp.next!=None:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
        print()

lst = LinkedList()
lst.append(10)
lst.append(20)
lst.append(30)
lst.append(40)
lst.append(50)
lst.append(60)
lst.append(70)
# lst.print_reverse()
# lst.remove_middle()
lst.display()
lst.swap_pairs()
lst.display()
# lst.displaySum()
# lst.displaySumOfAlternateNodes()
