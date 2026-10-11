# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # count=0
        # queue=deque([])
        # queue.append(root)
        # while len(queue)!=0:
        #     level_size=len(queue)
        #     count+=1
        #     for _ in range (level_size):
        #         el=queue.popleft()
        #         if el.left is not None:
        #             queue.append(el.left)
        #         if el.right is not None:
        #             queue.append(el.right)
        # return count

# Optimal
        def find(root):
            if root is None:
                return 0
            lh=find(root.left)
            rh=find(root.right)
            return 1+max(lh,rh)
        return find(root)

