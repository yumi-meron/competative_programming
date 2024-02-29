# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(curr):
            if curr == None:
                return None
            if curr.val < val:
                curr = search(curr.right)
            elif curr.val > val:
                curr = search(curr.left)
            
            return curr
        return search(root)