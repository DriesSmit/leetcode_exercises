# https://leetcode.com/problems/container-with-most-water/
from LeetCode.answer_checker import AnswerChecker

# Commonly used imports
from typing import List

# COPY CODE BELOW
class Solution:
    def calc_area(self, i, j):
        return (j-i)*min(self.height[i], self.height[j])

    def maxArea(self, height: List[int]) -> int:
        self.height = height
        max_area = 0
        for i in range(len(self.height)-1):
            for j in range(i+1, len(self.height)):
                area = self.calc_area(i, j)
                if area > max_area:
                    max_area = area
        
        return max_area
# COPY CODE ABOVE

if __name__ == "__main__":
    solution_instance = Solution()
    checker = AnswerChecker(solution_instance.maxArea, num_inputs=1)
    checker.check_all_cases(time_it=True)