# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = None
        curr = k
        
        def findSmallest(root):
            nonlocal smallest, curr
            if root == None:
                return 0

            findSmallest(root.left)
            curr -= 1
            if curr == 0:
                smallest = root.val
                return
            
            right = findSmallest(root.right)
            
            
        findSmallest(root)
        return smallest
        