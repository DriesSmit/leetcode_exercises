# https://leetcode.com/problems/jump-game-vi/
import sys
value_map = []
class Solution(object):
    @staticmethod
    def best_move_search(sub_nums, k):
        """
        :type sub_nums: List[int]
        :type k: int ()
        rtype: int (First index of a non-negative value, if there is no non-negative values return the last index.)
        """

        global value_map
        if len(sub_nums) == 1:
            return 0
        
        map_val = value_map[len(sub_nums)%len(value_map)]
        if map_val[1] is not None:
            if map_val[0]==len(sub_nums):
                return map_val[1]
       
        best_total = -sys.maxsize # Find a better init for this value.
        for i in range(1, min(k+1, len(sub_nums))):
            # Search over negative paths
            sub_total = sub_nums[i] + Solution.best_move_search(sub_nums[i: ], k)

            if sub_total >= best_total:
                best_total = sub_total

        value_map[len(sub_nums)%len(value_map)] = [len(sub_nums), best_total]
        return best_total
        

    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        global value_map
        value_map = [[None, None]]*k*2 # Is this k*2 correct?
        return nums[0] + Solution.best_move_search(nums, k)
        
if __name__ == "__main__":

    sol = Solution()

    total = sol.maxResult([1,-1,-2,4,-7,3], 2)
    assert  total==7, f"Got {total}"
    total = sol.maxResult([10,-5,-2,4,0,3], 3)
    assert total, f"Got {total}"
    total = sol.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)
    assert total == 0, f"Got {total}"
    # total = sol.maxResult(range(-1, -10001, -1), 2)
    # assert total == -25005001, f"Got {total}"