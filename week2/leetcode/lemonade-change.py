class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_of_5 = 0
        cnt_of_10 = 0
        for bill in bills:
            if bill == 5:
                cnt_of_5 += 1
            elif bill == 10:
                if cnt_of_5 > 0:
                    cnt_of_5 -= 1
                    cnt_of_10 += 1
                else:
                    return False
            else:
                if cnt_of_10 > 0 and cnt_of_5 > 0:
                    cnt_of_10 -= 1
                    cnt_of_5 -= 1
                elif cnt_of_5 >= 3:
                    cnt_of_5 -= 3
                else:
                    return False
        return True