# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        maxSum = 0
        def findMax(root, num):
            nonlocal maxSum
            if root:
                num = num * 10 + root.val
                if root.left == None and root.right == None:
                    maxSum += num
                    num -= root.val
                else:
                    left = findMax(root.left, num)
                    right = findMax(root.right, num)

        
        findMax(root, 0)
        return maxSum
            
        