class ListNode:
    def __init__(self, val=0,next=None):
        self.val=val
        self.next= next

class Solution:
    def startingpointofloop(self,head):
        slow=head
        fast=head

        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next

            if slow==fast:
                slow=head

                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow    
        return None

if __name__=="__main__":
    head= ListNode(1)
    head.next= ListNode(8)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)

    head.next.next.next.next=head.next

    sol= Solution()
    startpoint= sol.startingpointofloop(head)
    if startpoint:
        print("The loop started at ", startpoint.val)
    else:
        print("There is no loop")    

#Output:    The loop started at 8     