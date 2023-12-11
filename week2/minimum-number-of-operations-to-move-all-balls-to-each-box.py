class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        count = boxes.count('1')
        indices = [i for i in range(len(boxes)) if boxes[i] == '1']
        ans = []
        for i in range(len(boxes)):
            summ = 0
            for j in indices:
                summ += abs(i-j)
            ans.append(summ)
        return ans


            