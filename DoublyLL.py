class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.value)

class DoublyLL():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def prepend(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def traverse(self):
        current=self.head
        while current:
            print(current.value)
            current=current.next

    def reverse_traverse(self):
        current=self.tail
        while current:
            print(current.value)
            current=current.prev

    def get(self, index):
        if index<self.length/2:
            current=self.head
            count=0
            while count!=index:
                current=current.next
                count+=1
            return current
        else:
            current=self.tail
            count=self.length-1
            while count!=index:
                current=current.prev
                count-=1
            return current

    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            if temp.next is not None:
                result+= ' <-> '
            temp=temp.next
        return result
        

new=DoublyLL()
new.append(1)
new.append(2)
new.append(3)
new.prepend(0)
new.append(4)
#new.reverse_traverse()
print(new.get(4))