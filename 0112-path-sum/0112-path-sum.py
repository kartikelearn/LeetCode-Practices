# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        targetSum-=root.val
        if root.left is None and root.right is None:
            return targetSum==0
        return (self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum))



#        def recur(root, targetSum):
        #     if root.left is None and root.right is None:
        #         return targetSum == root.val
        #     elif root.left is None:
        #         return recur(root.right, targetSum-root.val)
        #     elif root.right is None:
        #         return recur(root.left, targetSum-root.val) 
        #     else:
        #         return recur(root.right, targetSum-root.val) or recur(root.left, targetSum-root.val)  
        
        # if root is None:
        #     return False
        # else:
        #     return recur(root, targetSum)
        