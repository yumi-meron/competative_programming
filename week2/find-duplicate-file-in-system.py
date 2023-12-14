class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for path in paths:
            path = path.split()
            for i in range(1,len(path)):
                file = path[i].split('(')
                dic[file[1]] = dic.get(file[1], [])
              
                dic[file[1]].append(path[0] + '/'+ file[0])
        ans = []    
        for key in dic:
            if len(dic[key]) > 1:
                ans.append(dic[key])
        return ans
        
            

        