class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data

class Doublly_list:
    
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.tail=newnode
            self.head.prev=None
            self.tail.next=None
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
            self.tail.next=None
    
    def pushany (self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        new_node.prev=temp

    def remove(self):
        self.head=self.head.next
        self.head.prev=None

    #def removelast(self):
        #self.tail=self.tail.prev
        #self.tail.next=None

    def removeany(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
        temp.next=temp.next.next
        temp.next.prev=temp

    def search (self,x):
        temp=self.head
        while temp!=None:
            if temp.data==x:
                return True
            temp=temp.next
        return False

    
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
              print(temp.data,"-->",end=" ")
              temp=temp.next

    def len(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

DLL=Doublly_list()
DLL.push(10)
DLL.push(20)
DLL.pushany(1,5)
DLL.pushany(3,30)
DLL.pushany(4,40)
#DLL.remove()
#DLL.removelast()
#DLL.removeany(3)
if DLL.search(10):
    print("yes")
else:
    print("No")
DLL.display()
print("\nlength of the linked list is: ", DLL.len())