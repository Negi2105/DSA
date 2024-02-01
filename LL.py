class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
    
class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1
    
    def prepend(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        
    def insert(self, index, value):
        new_node=Node(value)
        if index < 0 or index > self.length:
            print("Enter valid index")
            return False
        elif self.head is None:
            self.head=new_node
            self.tail=new_node
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
            while current:
                print(current.value)
                current = current.next

    def search(self, target):
        current = self.head
        count=0
        while current:
            count+=1
            if current.value==target:
                return count
            current = current.next
        return False
    
    def get(self, index):
        if index<0 or index>=self.length   :
            return ("Enter valid index")
            
        current = self.head
        for _ in range(index):
            current=current.next
        return current
    
    def set(self, index, value):
        if index<0 or index>=self.length   :
            return ("Enter valid index")
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def pop_first(self):
        if self.length==0:
            return None
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped_node.next=None
            self.length-=1
        return popped_node.value
    
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:    
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
            self.length-=1
        return popped_node
        
    def remove(self, index):
        current=self.head
        if index==0:
            return self.pop_first()
        if index>=self.length or index<0:
            return ("Index is out of range")
        if index==self.length-1:
            return self.pop().value
        #prev=self.get(index-1)
        for _ in range(index):
            prev=current
            current=current.next
        prev.next=current.next
        current.next=None
        self.length-=1
        return current.value
    
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
<<<<<<< HEAD
    
new=LinkedList()
new.append(10)
new.append(20)
new.append(30)
https://github.com/Negi2105/DSA
print(new) 
=======
>>>>>>> 8617936fc80f5e17966ab08c7f0ba1cb2a128acf

new_linkedlist= LinkedList()
#print(new_linkedlist.pop_first())
new_linkedlist.append(10)
new_linkedlist.append(20)
#new_linkedlist.append(30)
#new_linkedlist.append(40)
#new_linkedlist.prepend(0)
#print(new_linkedlist.search(40))
#print(new_linkedlist.get(2).value)
#new_linkedlist.set(3, 50)
#print(new_linkedlist.pop_first())
#print(new_linkedlist.pop().value)
print(new_linkedlist.remove(1))
print(new_linkedlist)
