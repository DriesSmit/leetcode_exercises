# https://leetcode.com/problems/jump-game-vi/
import sys
import numpy as np
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TODO: Potentially use modulus (e.g. arr is of size k) to save on memory here if needed 
        tot_arr = np.zeros(len(nums), dtype=np.int32)

        # Iterative backtrack solution
        tot_arr[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            best_total = -sys.maxsize # Find a better init for this value.
            for j in range(1, min(k+1, len(nums)-i)):
                cur_total = nums[i] + tot_arr[i+j]
                if cur_total > best_total:
                    best_total = cur_total
            tot_arr[i] = best_total
        return int(tot_arr[0])
        
if __name__ == "__main__":

    sol = Solution()
    total = sol.maxResult([1,-1,-2,4,-7,3], 2)
    assert  total==7, f"Got {total}"
    total = sol.maxResult([10,-5,-2,4,0,3], 3)
    assert total, f"Got {total}"
    total = sol.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)
    assert total == 0, f"Got {total}"
    total = sol.maxResult(range(-1, -10001, -1), 2)
    assert total == -25005001, f"Got {total}"