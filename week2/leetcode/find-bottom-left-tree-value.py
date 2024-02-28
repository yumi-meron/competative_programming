# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        bottomLeft = root.val
        def dfs(curr, depth):
            nonlocal maxDepth, bottomLeft
            if curr == None:
                return 0
            if depth > maxDepth:
                bottomLeft = curr.val
                maxDepth = depth
            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)
        dfs(root, 0)
        return bottomLeft
            