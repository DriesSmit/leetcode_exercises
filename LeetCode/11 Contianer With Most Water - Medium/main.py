# https://leetcode.com/problems/container-with-most-water/
from LeetCode.answer_checker import AnswerChecker

# Commonly used imports
from typing import List

# COPY CODE BELOW
class Solution:
    def calc_area(self, l, r):
        return (r-l)*min(self.height[l], self.height[r])

    def maxArea(self, height: List[int]) -> int:
        self.height = height
        left, right = 0, len(height)-1

        max_area = 0
        while left < right:
            area = self.calc_area(left, right)
            if area > max_area:
                max_area = area
            
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1

        return max_area
# COPY CODE ABOVE

if __name__ == "__main__":
    solution_instance = Solution()
    checker = AnswerChecker(solution_instance.maxArea, num_inputs=1)
    checker.check_all_cases(time_it=True)