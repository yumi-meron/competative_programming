# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        def insert(curr):
            if curr == None:
                return TreeNode(val)
            if val < curr.val:
                curr.left = insert(curr.left)
                return curr
            else:
                curr.right = insert(curr.right)
                return curr
        
        return insert(curr)


