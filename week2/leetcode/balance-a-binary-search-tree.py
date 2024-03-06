# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_list = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            sorted_list.append(root.val)
            inorder(root.right)

        inorder(root)
        
        def DAC(left, right):
            if left > right:
                return 
            mid = (left + right) // 2
            left_Node = DAC(left, mid-1)
            right_Node = DAC(mid + 1, right)

            return TreeNode(sorted_list[mid],left_Node, right_Node)

        return DAC(0, len(sorted_list)-1)
        