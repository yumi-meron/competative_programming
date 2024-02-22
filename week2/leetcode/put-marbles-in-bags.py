class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        minn = maxx = weights[0] + weights[-1]
        partitions = []
        for i in range(1, len(weights)):
            partitions.append(weights[i] + weights[i - 1]) 

        partitions.sort()
        # print(partitions)
        minn += sum(partitions[:k-1])
        maxx += sum(partitions[len(weights) - k:])
        # print(maxx, minn)

        return maxx - minn
        