class Listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addone(self, head: Listnode) -> Listnode:
        prev= None
        curr= head
        carry=1

        while curr:
                 