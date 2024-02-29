# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor(curr, p, q):
            if not curr:
                return None
            if curr == p or curr == q:
                return curr
            
            leftSide = ancestor(curr.left, p, q)
            rightSide = ancestor(curr.right, p, q)

            if not leftSide:
                return rightSide
            elif not rightSide:
                return leftSide
            else:
                return curr
                
        return ancestor(root,p,q)
             
            
            