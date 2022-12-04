class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circular_linkedlist:
    def __init__(self):
        self.head=node(None)
        self.tail=node(None)
        self.head.next=self.tail
        self.tail.next=self.head

    def push (self,data):
        new_node=node(data)
        
        if self.head.data is  None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head

        else:
            temp=self.head
            new_node.next=temp

            self.head=new_node
            self.tail.next=self.head

    def pushany (self,pos,data):
        new_node=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.data=data
        new_node.next=temp.next
        temp.next=new_node

    def pushlast(self,data):
        new_node=node(data)

        if self.head.data is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head
    
    def remove_first(self):
        if self.head!=self.tail:
            self.head=self.head.next
            self.tail.next=self.head
        else:
            self.head=self.tail=None

    def removeany (self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next

    

    def display(self):
        temp=self.head
        if self.head is not None:
            while True:
                print(temp.data,"-->",end=" ")
                temp=temp.next
                if temp==self.head:
                    break

    def search (self,x):
        temp=self.head
        while temp!=None:
            if temp.data==x:
                return True
            temp=temp.next
        return False

    def len (self):
        temp=self.head
        count=0
        if self.head!=None:
          while True:
            temp=temp.next
            count+=1
            if temp==self.head:
                break
        return count
    def removelast(self):
        p=self.head
        while (p.next!=self.tail):
            p=p.next
        self.tail=p
        p=p.next
        self.tail.next=self.head      
CL=circular_linkedlist()
CL.push(12)
CL.push(36)
CL.push(48)

CL.pushlast(10)
#CL.pushany(3,50)
#CL.remove_first()
#CL.removeany(4)
