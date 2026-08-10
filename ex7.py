class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
root=None
n=int(input("Enter the number of books:"))
for i in range(n):
    title=input("Enter the book title:")
    root=insert(root,title)
print("\nBooks in Inorder Traversal:")
inorder(root)
