class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        return sum(salary[1:n-1])/len(salary[1:n-1])
        