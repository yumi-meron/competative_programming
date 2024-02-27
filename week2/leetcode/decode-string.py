class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        
        def func(i):
            num = ""
            string = []
            while i < n and s[i] != ']':
                if s[i].isdigit():
                    num += s[i]

                elif s[i].isalpha():
                    string.append(s[i])

                elif s[i] == '[':
                    idx, st = func(i+1)
                    num = int(num) if num != "" else 1 
                    string.append(st * num)
                    num = ""
                    i = idx
                i+=1
            # i+=1
            # num = int(num) if num != "" else 0 
            return  (i, ''.join(string))



        return ''.join(func(0)[1])
                
                    
            
                
                

                    

