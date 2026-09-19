class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def loopdetect(self,head):
        slow=head
        fast= head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast= fast.next.next

            if (slow==fast):
                return True

        return False

def main():
    head= ListNode(1)
    second= ListNode(2)
    third= ListNode(3)
    fourth= ListNode(4)
    fifth= ListNode(5)

    head.next= second
    second.next= third
    third.next= fourth
    fourth.next= fifth
    fifth.next= third #loop

    solution= Solution()
    if solution.loopdetect(head):
        print("Loop detected in the linked list")
    else:
        print("There is no loop in the linkedlist")


if __name__== "__main__":
    main()
