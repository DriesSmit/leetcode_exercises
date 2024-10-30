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
# TODO: Keep going even if one has hit the k limit. There might still be better moves.
import numpy as np
class Solution(object):
    @staticmethod
    def handle_start(nums, spawn, left, right, cur_ones, moves, k, maxChanges):
        done = False

        # Check first left
        next_left = np.maximum(0, left - 1)
        should_check = (left!=next_left) * (cur_ones<k)
        cur_ones, moves = Solution.update_stats(nums, spawn, next_left, should_check, cur_ones, moves)
        left = next_left
        if np.all(cur_ones==k) or (np.sum(cur_ones==k) > 0 and np.all(moves >= np.min(moves[cur_ones==k]))):
            done = True

        if not done:
            # Right case
            next_right = np.minimum(len(nums)-1, right + 1)
            should_check = (right!=next_right) * (cur_ones<k)
            cur_ones, moves = Solution.update_stats(nums, spawn, next_right, should_check, cur_ones, moves)
            right = next_right
            if np.all(cur_ones==k) or (np.sum(cur_ones==k) > 0 and np.all(moves >= np.min(moves[cur_ones==k]))):
                done = True

        if not done:
            # Address the maxChanges case
            num_changes = np.minimum(k-cur_ones, maxChanges)
            cur_ones += num_changes
            moves += 2*num_changes # It takes two moves to use a change move


        return done, cur_ones, moves, left, right

    @staticmethod
    def update_stats(nums, spawn, locs, should_check, cur_ones, moves):
        result = should_check * nums[locs]
        cur_ones += result
        moves += result * np.abs(locs-spawn)
        return cur_ones, moves

    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        nums = np.array(nums, np.bool)
        zeros = np.zeros_like(nums)
        nums_big = np.concat([nums, zeros, zeros])
        spawn = np.arange(len(nums), dtype=np.int32)
        left = np.arange(len(nums), dtype=np.int32)
        right = np.arange(len(nums), dtype=np.int32)
        moves = np.zeros(len(nums), dtype=np.int32) # TODO: Is moves required or can it be calculated at the end?

        # Add premove start values
        cur_ones = np.array(nums, dtype=np.int32)

        # Handle the start seperately to make the rest of the code implementation simpler. 
        done, cur_ones, moves, left, right = Solution.handle_start(nums, spawn, left, right, cur_ones, moves, k, maxChanges)

        if not done:
            for _ in range(2, len(nums)):
                # TODO: Update this to multistep increases if needed
                # Left case
                left -= 1
                should_check = cur_ones<k
                cur_ones, moves = Solution.update_stats(nums_big, spawn, left, should_check, cur_ones, moves)
                result = cur_ones==k
                if np.all(result) or (np.any(result) > 0 and np.all(moves >= np.min(moves[result]))):
                    break

                # Right case
                right += 1
                should_check = cur_ones<k
                cur_ones, moves = Solution.update_stats(nums_big, spawn, right, should_check, cur_ones, moves)
                result = cur_ones==k
                if np.all(result) or (np.any(result) > 0 and np.all(moves >= np.min(moves[result]))):
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
    result = sol.minimumMoves([0,0], k=1, maxChanges=3)
    answer = 2
    assert result == answer, f"{result} not equal to {answer}" 

    # Test 4
    result = sol.minimumMoves([1,1], k=2, maxChanges=4)
    answer = 1
    assert result == answer, f"{result} not equal to {answer}" 

    # Test 5
    f = open("./Leetcode/3086_Minimum_Moves_Hard/example.txt", "r")
    nums, k, maxChanges = [line.strip() for line in f.readlines()]
    nums = [int(num) for num in nums[1:-3].split(",")]
    start = time.time()
    result = sol.minimumMoves(nums, k=int(k), maxChanges=int(maxChanges))
    end = time.time()
    print("result: ", result, ". Time (s): ", round(end-start, 2))
    # Laptop: time (s):  137.39
    # Parallel improved PC time (s): 4.25
    answer = 6828536
    assert result == answer, f"Calculated value {result} not equal to answer {answer}"

    # Test 6
    f = open("./Leetcode/3086_Minimum_Moves_Hard/example2.txt", "r")
    nums = [line.strip() for line in f.readlines()][0]
    nums = [int(num) for num in nums[1:-3].split(",")]
    start = time.time()
    result = sol.minimumMoves(nums, k=23886, maxChanges=15694)
    end = time.time()
    print("result: ", result, ". Time (s): ", round(end-start, 2))
    # Parallel improved PC time (s): 11.74
    answer = 33169542
    assert result == answer, f"Calculated value {result} not equal to answer {answer}" 

    