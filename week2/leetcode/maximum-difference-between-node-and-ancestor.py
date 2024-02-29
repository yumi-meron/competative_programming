# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxxDiff = float('-inf')
        def traverse(root):
            nonlocal maxxDiff
            
            minval = root.val
            maxval = root.val
            if not root.left and not root.right:
                return (root.val, root.val)

            if root.left:
                left = traverse(root.left)
                minn, maxx = left
                maxxDiff = max(maxxDiff, abs(minn - root.val), abs(maxx - root.val))
                minval = min(minval, minn)
                maxval = max(maxval, maxx)


                # maxxDiff = max(maxxDiff, abs(maxx - root.val))
            if root.right:
                right = traverse(root.right)
                minn, maxx = right
                maxxDiff = max(maxxDiff, abs(minn - root.val), abs(maxx - root.val))
                minval = min(minval, minn)
                maxval = max(maxval, maxx)
                

            return (minval,maxval)
        traverse(root)
        return maxxDiff
