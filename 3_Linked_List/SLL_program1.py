class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start
        
    def isEmpty(self):
        return self.start==None # is start is none which means list is empty

    def insert_at_start(self,data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.isEmpty():     
            temp = self.start
            while temp.next is not None:
                temp=temp.next
            temp.next = new_node
        else:
            self.start=new_node

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    # reference of the already stored element taken here in temp arg, data arg refers to value that is stored after the temp value
    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data,temp.next)
            temp.next = new_node

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        # check whether the list is empty
        if self.start is not None:      # No element in list
            pass

        # check whether the list contains only one ele
        elif self.start.next is None:
            self.start = None

        # check whether the list constains at least two ele
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next=None

    def delete_item(self,data):
        #if list is empty
        if self.start is None:
           pass
        # else if list contains one node ele
        elif self.start.next == None :
            if self.start.item == data:
                    self.start =None
        #else when list contains more than one node ele
        else:
            temp = self.start
            #IF the node is to be delete is the first node then
            if temp.item == data:
                self.start = temp.next
            else:
                # node after first node 
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next



# class SLL_Iterable:
#     def __init__(self,start):
#         self.current = start

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data=self.current.item
#         self.current = self.current.next
            



# Driver code
myList=SLL()
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_last(10)
myList.insert_after(myList.search(20),45)
myList.print_list()
print()

myList.delete_item(20)
print()
myList.print_list()

myList.delete_item(10)
print()
myList.print_list()

# # iterable loop to print list node elements
# for x in myList:
#     print(x,ends=' ')# this code snippet gives error that Sll is not iterable



# print(f'searing node : {myList.search(30)}')
# print('hello')