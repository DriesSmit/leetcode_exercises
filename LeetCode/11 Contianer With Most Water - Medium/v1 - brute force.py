# https://leetcode.com/problems/container-with-most-water/
from LeetCode.answer_checker import AnswerChecker

# Commonly used imports
from typing import List

# COPY CODE BELOW
class Solution:
    def calc_area(self, i, j):
        return abs(self.locs[j]-self.locs[i])*min(self.height[i], self.height[j])

    def maxArea(self, height: List[int]) -> int:
        # Single sort operation based on values in `height`
        self.locs = sorted(range(len(height)), reverse=True, key=lambda k: height[k])
        # Create a sorted version of `height` using the sorted indices from `locs`
        self.height = [height[k] for k in self.locs]

        max_area = 0
        for i in range(len(self.height)-1):
            max_w = max(self.locs[i], len(self.height)-1-self.locs[i])
            max_pos_i_area = self.height[i]*max_w
            if max_pos_i_area > max_area:
                for j in range(i+1, len(self.height)):
                    if self.height[j]*max_w <= max_area:
                        break

                    area = self.calc_area(i, j)
                    if area > max_area:
                        max_area = area
        
        return max_area
# COPY CODE ABOVE

if __name__ == "__main__":
    # Time to beat: 8.4 s
    solution_instance = Solution()
    checker = AnswerChecker(solution_instance.maxArea, num_inputs=1)
    checker.check_all_cases(time_it=True)