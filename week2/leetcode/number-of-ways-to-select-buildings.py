class Solution:
    def numberOfWays(self, s: str) -> int:
        # preZ = [0] * len(s)
        # preO = [0] * len(s)
        # for i in range(len(s)):
        #     if s[i] == '0':
        #         preZ[i] = 1
        #     else:
        #         preO[i] = 1
        
        # for i in range(1,len(s)):
        #     preZ[i] += preZ[i-1]
        #     preO[i] += preO[i-1]
        # # print(preZ)
        # # print(preO)
        # n01 = [0] * len(s)
        # n10 = [0] * len(s)
        # for i in range(len(s)):
        #     if s[i] == '1':
        #         n01[i] = preZ[i]
        #     else:
        #         n10[i] = preO[i]
        # for i in range(1,len(n01)):
        #     n01[i] += n01[i-1]
        #     n10[i] += n10[i-1]
        
        # n010 = [0] * len(s)
        # n101 = [0] * len(s)
        # for i in range(len(s)):
        #     if s[i] == '0':
        #         n010[i] += n01[i]
        #     else:
        #         n101[i] += n10[i]

        # for i in range(1,len(n010)):
        #     n010[i] += n010[i-1]
        #     n101[i] += n101[i-1]

        # return n101[-1] + n010[-1]

        ones = zeros = oneZero = zeroOne = 0
        ans = 0
        for num in s:
            if num == '0':
                zeros += 1
                oneZero += ones
                ans += zeroOne
            else:
                ones += 1
                zeroOne += zeros
                ans += oneZero
        return ans
        
 
