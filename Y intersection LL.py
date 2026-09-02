class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def insertatend(head,val):
    newNode=Node(val)
    if head is None:
        return newNode
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.next=newNode
    return head

def printlist(head):
    while head and head.next is not None:
        print(head.val,end="->")
        head=head.next
    if head:
        print(head.val)

def getdifference(head1,head2):
    c1=c2=0
    while head1 is not None:
        c1+=1
        head1=head1.next
    while head2 is not None:
        c2+=1
        head2=head2.next
    return c1-c2    

def yintersection(head1, head2):
    
    diff=getdifference(head1,head2)
    if(diff<0):
        while diff !=0:
            head2=head2.next
            diff+=1
    else:
        while diff!=0:
            head1=head1.next
            diff-=1
    while head1 is not None and head2 is not None:
        if head1==head2:
            return head1
        head1=head1.next
        head2=head2.next
    return None


head = Node(1)
head = insertatend(head, 3)
head = insertatend(head, 1)
head = insertatend(head, 2)
head = insertatend(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing the lists
print("List1: ", end="")
printlist(head1)
print("List2: ", end="")
printlist(head2)

# Checking if intersection is present
answerNode = yintersection(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.val}")

