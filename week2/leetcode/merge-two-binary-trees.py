# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(curr1, curr2):
            if curr1 == None and curr2 == None:
                return None

            elif not curr1 :
                return curr2
                
            elif not curr2:
                return curr1
            
            curr1.val += curr2.val

            curr1.left = merge(curr1.left, curr2.left)
            curr1.right = merge(curr1.right, curr2.right)

            return curr1
        
        return merge(root1, root2)
            