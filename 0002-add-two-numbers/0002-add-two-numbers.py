# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def helper(l1,l2,carry):
            if not l1 and not l2 and carry==0:
                return None
            total=carry
            if l1:
                total+=l1.val
            if l2:
                total+=l2.val
            node=ListNode(total%10)
            node.next=helper(l1.next if l1 else None, l2.next if l2 else None, total//10)

            return node
        return helper(l1,l2,0)

# dummy = ListNode(0)
# curr = dummy

# while l1 or l2 or carry:
#     total = carry

#     if l1:
#         total += l1.val
#         l1 = l1.next

#     if l2:
#         total += l2.val
#         l2 = l2.next

#     digit = total % 10
#     carry = total // 10

#     curr.next = ListNode(digit)
#     curr = curr.next

# return dummy.next