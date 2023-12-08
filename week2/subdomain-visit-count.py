class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains:
            num = int(domain.split()[0])
            string = domain.split()[1].split('.')
           
            for i in range(len(string)):
                temp = '.'.join(string[i:])
                dic[temp] = dic.get(temp, 0) + num
        ans = [f"{value} {key}" for key,value in dic.items()]
        return ans

            
        