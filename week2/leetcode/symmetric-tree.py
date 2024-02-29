# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            if left.val != right.val:
                return False
            elif left.val == right.val:
                first = traverse(left.left, right.right)
                second = traverse(left.right, right.left)
                if first and second:
                    return True
                else:
                    return False
            # else:
            #     return False
        return traverse(root.left, root.right)
