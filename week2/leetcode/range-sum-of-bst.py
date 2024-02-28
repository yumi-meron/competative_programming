# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # nums = []
        # def traverse(root):
        #     if root == None:
        #         return 
        #     traverse(root.left)
        #     nums.append(root.val)
        #     traverse(root.right)
        # traverse(root)
        # print(nums)
        # summ = 0
        # for num in nums:
        #     if num >= low and num <= high:
        #         summ += num
        # return summ
        summ = 0
        def traverse(root):
            nonlocal summ
            if root == None:
                return 
            if low<= root.val <= high:
                summ += root.val
            traverse(root.left)
            # nums.append(root.val)
            traverse(root.right)
        traverse(root)
        return summ

        