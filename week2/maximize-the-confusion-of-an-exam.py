class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        mp = {'T': 0, 'F': 0}
        left,ans = 0,0
        for right in range(len(answerKey)):
            mp[answerKey[right]] += 1

            while mp['T'] > k and mp['F'] > k:
                mp[answerKey[left]] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)

        return ans



        