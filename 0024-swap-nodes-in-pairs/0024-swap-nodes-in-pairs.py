# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        result=ListNode(0)
        result.next=head
        prev=result
        while prev.next and prev.next.next is not None:
            first=prev.next
            second=first.next
            NextNode=second.next

            first.next=NextNode
            second.next=first
            prev.next=second
            prev=first
        return result.next
            