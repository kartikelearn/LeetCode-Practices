from functools import cache
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @cache
    def reverseList(self, head: ListNode | None) -> ListNode | None:
    
        # do it on copy-pen then it will be right


        # prev=None
        # curr=head
        # while curr is not None:
        #     next=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=next
        # return prev

        #Brute

        # temp = head # temp is basically the current node
        # stack=[]
        # while temp is not None:
        #     stack.append(temp.val)
        #     temp=temp.next
        # temp=head
        # while temp is not None:
        #     el=stack.pop()
        #     temp.val=el
        #     temp=temp.next
        # return head

# Average
        if head is None or head.next is None:
            return head
        prev=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return prev

        