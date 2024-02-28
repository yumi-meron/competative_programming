# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(curr):
            while curr and curr.left:
                curr = curr.left
            return curr

        def delete(curr, key):
            if curr == None:
                return None

            if curr.val > key:
                curr.left = delete(curr.left, key)
            elif curr.val < key:
                curr.right = delete(curr.right, key)
            else:
                if not curr.left:
                    return curr.right
                elif not curr.right:
                    return curr.left
                else:
                    minNode = minValueNode(curr.right)
                    curr.val = minNode.val
                    curr.right = delete(curr.right, minNode.val)

            return curr
        
        return delete(root, key)




