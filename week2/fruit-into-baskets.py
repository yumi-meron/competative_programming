class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left,ans,mp = 0, 0, {}

        for right in range(len(fruits)):
            mp[fruits[right]] = mp.get(fruits[right], 0) + 1
            while len(mp) > 2:
                if mp[fruits[left]] - 1 == 0:
                    del mp[fruits[left]]
                else:
                    mp[fruits[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)


        return ans
        