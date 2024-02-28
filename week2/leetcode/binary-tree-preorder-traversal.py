# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preOrder = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        if curr == None:
            return 
        self.preOrder.append(curr.val)
        self.preorderTraversal(curr.left)
        self.preorderTraversal(curr.right)
        return self.preOrder


