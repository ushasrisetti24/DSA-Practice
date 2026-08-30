class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next

class Solution:
    def Lengthofloop(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                slow=slow.next
                cnt=1
                while slow!=fast:
                    cnt+=1
                    slow=slow.next
                return cnt

                  
        return None       

if __name__ == "__main__":
    # Creating a sample linked list with a loop
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Linking the nodes
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # Creating a loop from fifth to second
    fifth.next = second

    # Creating a Solution object
    obj = Solution()

    # Getting the loop length
    loopLength = obj.Lengthofloop(head)

    # Printing the result
    if loopLength > 0:
        print("Length of the loop:", loopLength)
    else:
        print("No loop found in the linked list.")