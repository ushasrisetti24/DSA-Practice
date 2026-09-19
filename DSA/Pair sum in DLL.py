class DNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

def insertNodes(head,val):
    newnode=DNode(val)
    if head is None:
        return newnode

    curr=head
    while curr.next:
        curr=curr.next
        
    curr.next=newnode
    newnode.prev=curr
    return head    
        

            


def pairsumdll(head,key):
    if head is None:
        return None

    p1=head
    p2=head
    pair=[]
    while p2.next is not None:
        p2=p2.next

    while p1.next is not None and p1!=p2:
        if(p1.val + p2.val==key):
            pair.append((p1.val,p2.val))
            p1=p1.next
            p2=p2.prev
        elif (p1.val + p2.val)>key:
            p2=p2.prev
        elif(p1.val + p2.val)<key:
            p1=p1.next

    return pair            


if __name__=="__main__":
    arr= [1,2,4,5,6,8,9]
    key=7
    head = DNode(arr[0])
    head.next = DNode(arr[1])
    head.next.prev = head
    head.next.next = DNode(arr[2])
    head.next.next.prev = head.next
    head.next.next.next = DNode(arr[3])
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = DNode(arr[4])
    head.next.next.next.next.prev = head.next.next.next
    head.next.next.next.next.next= DNode(arr[5])
    head.next.next.next.next.next.prev = head.next.next.next.next
    head.next.next.next.next.next.next= DNode(arr[6])
    head.next.next.next.next.next.next.prev = head.next.next.next.next.next
    
    result= pairsumdll(head,key)
    print(result)
    
            
        


