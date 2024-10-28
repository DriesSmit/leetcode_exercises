# https://leetcode.com/problems/jump-game-vi/

class Solution(object):
    def best_move_search(self, sub_nums, k):
        """
        :type sub_nums: List[int]
        :type k: int ()
        rtype: int (First index of a non-negative value, if there is no non-negative values return the last index.)
        """
        
        if len(sub_nums) > 1:
            best_path, best_total = None, -10**10 # Find a better init for this value.
            for i in range(1, min(k+1, len(sub_nums))):
                if sub_nums[i] < 0:
                    # Search over negative paths
                    sub_path, sub_total = self.best_move_search(sub_nums[i: ], k)
                    sub_total += sub_nums[i]
                    
                    if sub_total >= best_total:
                        best_path, best_total = [i] + sub_path, sub_total
                else:
                    # Found the closest positive value. Move to that value.
                    best_path, best_total = [i], sub_nums[i]
                    break
        else:
            # Only one option. Take that option.
            assert len(sub_nums) == 1
            best_path, best_total = [], 0
        
        return best_path, best_total
        

    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        total = nums[0]
        n = len(nums)
        total_path = []
        while count < n-1:
            path, score = self.best_move_search(nums[count:], k)
            total_path.extend(path)
            total += score
            count += sum(path)
            
            
        return total
        
if __name__ == "__main__":

    sol = Solution()

    # total = sol.maxResult([1,-1,-2,4,-7,3], 2)
    # assert  total==7, f"Got {total}"
    # total = sol.maxResult([10,-5,-2,4,0,3], 3)
    # assert total, f"Got {total}"
    # total = sol.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)
    # assert total == 0, f"Got {total}"
    total = sol.maxResult(range(-1, -10001, -1), 2)
    assert total == 0, f"Got {total}"