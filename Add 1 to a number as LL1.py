class Node:
    def __init__(self,val):
        self.val=val
        self.next= None

def reverselist(head):
    prev= None
    curr=head
    while curr is not None:
        nextnode=curr.next
        curr.next= prev
        prev=curr
        curr= nextnode
    return prev
class Solution:
    def addone(self,head):
        if head is None:
            return Node(1)
        newNode=Node(0)
        temp=newNode
        curr= reverselist(head)
        carry=1
        sum=0
        while curr is not None:
            sum=curr.val
            sum+=carry
            temp.next= Node(sum%10)
            carry= sum//10
            temp=temp.next
            curr=curr.next
            sum=0

        if carry>0:
            temp.next=Node(carry)
        return reverselist(newNode.next)

def printaddnode(head):
    while head is not None:
        print(head.val, end="->")
        head = head.next

if __name__=="__main__":
    head=Node(1)
    head.next=Node(8)
    head.next.next=Node(9)
    head.next.next.next=Node(9)
sol=Solution()
result=sol.addone(head)
printaddnode(result)

