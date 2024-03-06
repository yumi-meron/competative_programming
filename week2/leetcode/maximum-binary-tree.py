# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(nums):
            if not nums:
                return 
            mp = {}
            for i,num in enumerate(nums):
                mp[num] = i
            
            maxx = max(nums)
            idx = mp[maxx]
            left_part = build(nums[:idx])
            right_part = build(nums[idx + 1:])

            return TreeNode(nums[idx], left_part, right_part)
        return build(nums)