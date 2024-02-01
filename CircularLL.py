class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
        
    def __str__(self):
        return str(self.value)

class CircularLL():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def append(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
        
    def prepend(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1
        
    def insert(self, index, value):
        new_node=Node(value)
        if index < 0 or index > self.length:
            print("Enter valid index")
            return False
        elif self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        elif index==0:
            self.prepend(value)
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return True    
    
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if current==self.head:
                break
                
    def search(self, target):
        current=self.head
        count=0
        while current is not None:
            if current.value==target:
                return count
            else:
                current=current.next
                count+=1
            if current==self.head:
                return "Element is not present"
            
    def remove(self, index):
        current=self.head
        for _ in range(index):
            prev=current
            current=current.next
        prev.next=current.next
        current.next=None
        self.length-=1
        return current
    
    def delete_all(self):
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
        
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node=temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
        
new=CircularLL()
new.prepend(5)
new.prepend(6)
new.append(7)
new.insert(1, 50)
new.traverse()
new.search(5)
print(new)
new.remove(1)
print(new)