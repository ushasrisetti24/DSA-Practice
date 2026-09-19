class DNode:
    def __init__(self,val):
        self.val=val
        self.next= None
        self.prev=None

def deletekey(head,key):
    if head is None:
        return None
    curr=head
    
    while curr is not None:
        nextnode=curr.next

        if curr.val==key:
            if curr.prev is None:
                head=curr.next
            else:
                curr.prev.next= curr.next
            if curr.next is not None:
                curr.next.prev= curr.prev

        curr=curr.next
    return head                    


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    key = 3

    # Create doubly linked list manually
    head = DNode(arr[0])
    head.next = DNode(arr[1])
    head.next.prev = head
    head.next.next = DNode(arr[2])
    head.next.next.prev = head.next
    head.next.next.next = DNode(arr[3])
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = DNode(arr[4])
    head.next.next.next.next.prev = head.next.next.next

    # Delete the nodes with the specified key
    head = deletekey(head, key)
    while head is not None:
        print(head.val, end=" ")
        head = head.next       
        

        