class Node:
    def __init__(self,prev=None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        new_node = Node(None,data,self.start) 
        if not self.start == None:  
            self.start.prev=new_node
        self.start = new_node #if list is empty thn excute it

    def insert_at_last(self,data):
        temp = self.start
        if self.start is not None:          # list is not empty
            while temp.next is not None:   
                temp = temp.next
            # new_node = Node(temp,data,None)
            # temp.next = new_node
        # else:
        #     new_node = Node(None,data,None)
        #     self.start = new_node
        # OR
        new_node = Node(temp,data,None)
        if temp == None:                    # means list is empty
            self.start=new_node
        else:                               # means list is not empty temp contains last node
            temp.next = new_node

    def search(self,data):
        temp = self.start
        while temp.next is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            new_node = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node

    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item,end=' ')
                temp = temp.next
        else:
            print("DLL is empty")

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp=temp.next

            


#  Driver Code
dll = DLL()
dll.insert_at_start(30)
dll.insert_at_start(40)
dll.insert_at_last(20)
dll.insert_at_last(21)
dll.insert_at_last(22)
dll.insert_at_last(23)
dll.insert_at_last(24)
dll.print_list()