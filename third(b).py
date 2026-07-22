class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        print(data ,"added to the stack")
    def pop(self):
        if self.top is None:
            print("Stack Underflow! No books to remove")
        else:
            temp=self.top
            self.top=self.top.next
            print(temp.data," removed from the stack")
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp=self.top
            print("Stack elements (Top to bottom):")
            while temp:
             print(temp.data,end="-->")
             temp=temp.next
            print("Null")    
stack=stack()
while True:
    print("-----STACK USING LINKED LIST-----")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Enter Your choice:"))
    if choice==1:
        book=input("Enter Book title:")
        stack.push(book)
    elif choice==2:
        stack.pop()
    elif choice==3:
        stack.display()
    elif choice==4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
