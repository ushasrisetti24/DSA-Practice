class Node:
    def __init__(self,val):
        self.val=val
        self.next= None

def printLL(head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next

def deletenend(head,n):
    if head is None:
        return None
    dummy=Node(0)
    dummy.next=head
    slow=fast=dummy
    c=1 
    curr=head
    while curr.next is not None:    
        c+=1
        curr=curr.next
    for i in range(c-n+1): fast=fast.next

    while fast.next is not None:
        slow=slow.next
        fast=fast.next
    slow.next= slow.next.next    
    return dummy.next

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # Create Solution object
   

    # Delete the Nth node from the end
    head = deletenend(head, N)

    # Print the modified linked list
    printLL(head)