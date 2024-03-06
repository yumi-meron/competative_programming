# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mp = defaultdict(list)
        level = 0
        def BFS(root):
            queue = deque()
            if root:
                mp[0].append(1)
                queue.append((0,root))
            level = 0
            # curr_val = 0
            while queue:
                for i in range(len(queue)):
                    idx , curr = queue.popleft()
            
                    if curr.left:
                        curr_idx = (idx) * 2 + 1
                        
                        mp[level+1].append(curr_idx)
                        queue.append((curr_idx,curr.left))
                    if curr.right:
                        curr_idx = (idx) * 2 + 2
                        mp[level+1].append(curr_idx)
                        queue.append((curr_idx,curr.right))
                level += 1
        BFS(root)
        # print(mp)

        max_width = float('-inf')
        for key in mp:
            max_width = max(max_width, (mp[key][-1] - mp[key][0] + 1))
        return max_width

        