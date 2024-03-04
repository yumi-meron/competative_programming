# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: 
        def build(left,right):
            if left > right:
                return None

            mid = (left + right)//2
            left_part = build(left, mid-1)
            right_part = build(mid+1, right)

            return TreeNode(nums[mid], left_part, right_part)

        return build(0, len(nums)-1)

            