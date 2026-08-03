class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None
def insert(head, coeff, power):
    new = Node(coeff, power) 
    if head is None:
        return new
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new
    return head
def addPoly(p1, p2):
    result = None
    while p1 and p2:
        if p1.power == p2.power:
            if (p1.coeff + p2.coeff) != 0:
                result = insert(result, p1.coeff + p2.coeff, p1.power)
            p1 = p1.next
            p2 = p2.next
        elif p1.power < p2.power:
            result = insert(result, p1.coeff, p1.power)
            p1 = p1.next
        else:
            result = insert(result, p2.coeff, p2.power)
            p2 = p2.next
    while p1:
        result = insert(result, p1.coeff, p1.power)
        p1 = p1.next
    while p2:
        result = insert(result, p2.coeff, p2.power)
        p2 = p2.next
    return result
def display(head):
    if head is None:
        print("0")
        return
    while head:
        print(f"{head.coeff}x^{head.power}", end=" ")
        if head.next:
            print("+", end=" ")
        head = head.next
    print()
def create_polynomial(poly_num):
    head = None
    print(f"\n*** Creating a Polynomial ***")
    try:
        num_terms = int(input("Enter the number of terms: "))
    except ValueError:
        print("Invalid number. Creating an empty polynomial.")
        return head
    for i in range(num_terms):
        print(f"Term {i+1}:")
        try:
            coeff = int(input("  Enter the coefficient: "))
            power = int(input("  Enter the power: "))
            head = insert(head, coeff, power)
        except ValueError:
            print("  Invalid input! Skipping this term.")
    return head
p1 = create_polynomial(1)
p2 = create_polynomial(2)
print("\nPolynomial 1:")
display(p1)
print("Polynomial 2:")
display(p2)
result = addPoly(p1, p2)
print("\nResultant Polynomial:")
display(result)
