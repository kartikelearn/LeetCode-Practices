# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr=None, head
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev


        # if head==None:
        #     return None
        # newHead=head
        # if head.next!=None:
        #     newHead=self.reverseList(head.next)
        #     head.next.next=head
        # head.next=None
        # return newHead

        