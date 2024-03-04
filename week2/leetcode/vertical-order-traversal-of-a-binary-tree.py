# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        def BFS(root):
            queue = deque()
            if root:
                queue.append((0, root))
            # ver_idx = 0
            level = 0
            while queue:
                for i in range(len(queue)):
                    idx, curr = queue.popleft()
                    mp[idx].append((level,curr.val))
                    if curr.right:
                        queue.append((idx+1, curr.right))
                    if curr.left:
                        queue.append((idx-1,curr.left))
                level += 1
                    
        BFS(root)
        tuples  = []
        sorted_map = sorted(mp)
        for key in sorted_map:
            tuples.append(sorted(mp[key]))
        # print(tuples)
        ans = []
        for lst in tuples:
            temp = []
            for i in range(len(lst)):
                temp.append(lst[i][1])
            ans.append(temp)
        return ans

                    



