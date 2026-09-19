class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def sort012(self,head):
        if head is None:
            return None
        l0=t0= Node(0)
        l1=t1= Node(0)
        l2=t2=Node(0)

        while head is not None:
            newnode=Node(head.val)
            if head.val==0:
                t0.next=newnode
                t0=t0.next
            elif head.val==1:
                t1.next=newnode
                t1=t1.next
            elif head.val==2:
                t2.next=newnode
                t2=t2.next
            else:
                continue
            head=head.next
        t0.next= l1.next
        t1.next= l2.next
        t2.next=None
        return l0.next


def printlist(head):
    while head is not None:
        print(head.val, end="->")
        head=head.next  

if __name__=="__main__":
    
    head=Node(0)
    head.next=Node(1)
    head.next.next=Node(2)
    head.next.next.next=Node(0)
    head.next.next.next.next=Node(1)
    head.next.next.next.next.next=Node(2)
    sol=Solution()
    result=sol.sort012(head)
    printlist(result)        