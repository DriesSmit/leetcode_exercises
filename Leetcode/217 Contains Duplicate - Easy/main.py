# https://leetcode.com/problems/contains-duplicate/
from answer_checker import AnswerChecker

# Commonly used imports
from typing import List

# COPY CODE BELOW
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True
# COPY CODE ABOVE

if __name__ == "__main__":
    checker = AnswerChecker(Solution.containsDuplicate, num_inputs=1)
    checker.check_all_cases()