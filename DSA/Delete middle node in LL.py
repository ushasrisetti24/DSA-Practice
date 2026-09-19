class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        slow= head
        fast=head.next.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        slow.next= slow.next.next            
        return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

# Driver function
if __name__ == "__main__":
    # Creating linked list 1->2->3->4->5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Printing original list
    print("Original Linked List:", end=" ")
    printLL(head)

    # Deleting middle node
    obj = Solution()
    head = obj.deleteMiddle(head)

    # Printing updated list
    print("Updated Linked List:", end=" ")
    printLL(head)    