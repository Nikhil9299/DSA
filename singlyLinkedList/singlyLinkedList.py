class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlly_linkedlist:

    def __init__(self):
        self.head=None

# adding data in singlly linked list
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

#add anywhere in singlly linked list
    def pushany (self,pos,data):
        new_node=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.data=data
        new_node.next=temp.next
        temp.next=new_node

#adding data to the last of linked list
    def pushlast(self,data):
        new_node=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def remove_first (self):  #removing 1st data
        temp=self.head
        self.head=temp.next
        temp.next=None

    def remove_anyposition (self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next

    def remove_last(self):
        temp=self.head.next
        prev=self.head

        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    

    
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

L=singlly_linkedlist()
L.push(40)
L.push(30)
L.push(20)
L.push(10)
L.pushany(4,50)
L.pushlast(60)
#L.remove_first()
L.remove_anyposition(2)
#L.remove_last()
if L.search(10):
    print("yes")
else:
    print("No")
L.display()
print("\nlength of the linked list is: ", L.len())