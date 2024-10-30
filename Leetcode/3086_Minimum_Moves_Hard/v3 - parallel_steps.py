# https://leetcode.com/problems/minimum-moves-to-pick-k-ones
# from tqdm import tqdm
import time

# Options
# 1) Assume always using all maxChanges, seperate case when not.
# 2) Search areas at the same time (left==right) by expanding the length up until we hit k using binary search.
# 3) Then only calculate the moves by doing one big multiplication.
# 4) Optional last performance improvement. Do this for all starting points at the same time.
# 5) Cache the previous results. We can control max window to a max size.

# Space complexity O(n)?
# Memory complexity O(n)?
# Do we need to calculate moves per turn?

# Variables:

# rad : int
# k: int
# maxChanges: int
# nums: array of size n
# left: array of size n
# right: array of size n
# ones: array of size n
# moves (optional): array of size n


# COPY BELOW
import numpy as np
class Solution(object):
    @staticmethod
    def update_stats(nums, spawn, locs, updated, cur_ones, moves):
        cur_ones += updated * nums[locs]
        moves += updated * np.abs(locs-spawn) * nums[locs]
        return cur_ones, moves

    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        nums = np.array(nums, np.bool)
        spawn = np.arange(len(nums), dtype=np.int32)
        left = np.arange(len(nums), dtype=np.int32)
        right = np.arange(len(nums), dtype=np.int32)
        moves = np.zeros(len(nums), dtype=np.int32) # TODO: Is moves required or can it be calculated at the end?

        # Add premove start values
        cur_ones = np.array(nums[spawn], dtype=np.int32)
        for rad in range(1, len(nums)):
            if rad == 2:
                # Address the maxChanges case
                if np.all(k-cur_ones > maxChanges):
                    cur_ones += maxChanges
                    moves += 2*maxChanges # It takes two moves to use a change move
                else:
                    # maxChanges is enough to find min moves
                    min_add = np.min(k-cur_ones)
                    cur_ones += min_add
                    moves += 2*min_add
                    break
            else:
                # TODO: Update this to multistep increases if needed
                # Left case
                next_left = np.maximum(0, left - 1)
                cur_ones, moves = Solution.update_stats(nums, spawn, next_left, left!=next_left, cur_ones, moves)
                left = next_left
                if np.any(cur_ones==k):
                    break

                # Right case
                next_right = np.minimum(len(nums)-1, right + 1)
                cur_ones, moves = Solution.update_stats(nums, spawn, next_right, right!=next_right, cur_ones, moves)
                right = next_right
                if np.any(cur_ones==k):
                    break
        return int(np.min(moves[cur_ones==k]))
# COPY ABOVE

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    result = sol.minimumMoves([1,1,0,0,0,1,1,0,0,1], k=3, maxChanges=1)
    answer = 3
    assert result == answer, f"{result} not equal to {answer}"

    # Test 2
    result = sol.minimumMoves([0,0,0,0], k=2, maxChanges=3)
    answer = 4
    assert result == answer, f"{result} not equal to {answer}" 

    # Test 3
    f = open("./Leetcode/3086_Minimum_Moves_Hard/example.txt", "r")
    nums, k, maxChanges = [line.strip() for line in f.readlines()]
    nums = [int(num) for num in nums[1:-3].split(",")]
    start = time.time()
    result = sol.minimumMoves(nums, int(k), int(maxChanges))
    end = time.time()
    print("result: ", result, ". Time (s): ", round(end-start, 2))
    # Laptop: time (s):  137.39
    # Parallel improved PC time (s): 3.99
    answer = 6828536
    assert result == answer, f"{result} not equal to {answer}" 

    