class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def segregateoddeven(self,head):
        if head is None or head.next is None:
            return head

        Evenhead= Eventail= None
        Oddhead= Oddtail= None

        current= head

        while current:
            if current.val % 2==0:
                if not Evenhead:
                    Evenhead= Eventail= current
                else:
                    Eventail.next= current
                    Eventail=current
                    
            else:
                if not Oddhead:
                    Oddhead= Oddtail=current
                else:
                    Oddtail.next=current
                    Oddtail=current
            current=current.next       

        if not Evenhead:
            return Oddhead                        
        if not Oddhead:
            return Evenhead

        Eventail.next=Oddhead
        Oddtail.next= None
        return Evenhead

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)

sol = Solution()
newHead = sol.segregateoddeven(head)
printList(newHead)
                          