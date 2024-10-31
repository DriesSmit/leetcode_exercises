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


# TO SPEED THIS UP
# Use nums.cumsum to be able to quickly calculate sums between two values.
# Do the same for moves. For moves you will have to use the nums.cumsum value to get the correct moves addition.



# COPY BELOW
# TODO: Keep going even if one has hit the k limit. There might still be better moves.
import numpy as np
class Solution(object):
    @staticmethod
    def check_end_condition(cur_ones, moves, k, rad):
        # TODO: One could potentially squeeze out a bit more performance by improving the estimate 
        # for the minimum possible score, which may reduce unnecessary computations.
        equal = cur_ones==k
        less = cur_ones<k
        result_sum = np.sum(equal)
        if result_sum > 0 and np.all((np.min(moves[equal])-moves[less]) <= rad*(k - cur_ones[less])):
            return True
        return False
    
    @staticmethod
    def handle_start(nums, spawn, left, right, cur_ones, moves, k, maxChanges):
        # Check first left
        next_left = np.maximum(0, left - 1)
        should_check = (left!=next_left) * (cur_ones<k)
        cur_ones, moves = Solution.update_stats(nums, spawn, next_left, should_check, cur_ones, moves)
        left = next_left
        done = Solution.check_end_condition(cur_ones, moves, k, 1)

        if not done:
            # Right case
            next_right = np.minimum(len(nums)-1, right + 1)
            should_check = (right!=next_right) * (cur_ones<k)
            cur_ones, moves = Solution.update_stats(nums, spawn, next_right, should_check, cur_ones, moves)
            right = next_right
            done = Solution.check_end_condition(cur_ones, moves, k, 1)

        if not done:
            # Address the maxChanges case
            num_changes = np.minimum(k-cur_ones, maxChanges)
            cur_ones += num_changes
            moves += 2*num_changes # It takes two moves to use a change move
            done = Solution.check_end_condition(cur_ones, moves, k, 2)

        return done, cur_ones, moves, left, right

    @staticmethod
    def update_stats(nums, spawn, locs, should_check, cur_ones, moves):
        cur_ones += should_check * nums[locs]
        moves += should_check * np.abs(locs-spawn) * nums[locs]
        return cur_ones, moves

    @staticmethod
    def update_batched_stats(spawn, start, end, cur_ones, moves, k, cumsum_nums, cumsum_moves, neg_cumsum_moves, side):
        # Note: Start is always the closest point to spawn and end further away or equal.
        update = cur_ones < k
        cur_ones += update * (cumsum_nums[end+1]-cumsum_nums[start])
        
        if side == "left":
            r_start = len(moves) - start - 1
            r_end = len(moves) - end - 1
            r_spawn = len(moves) -spawn

            print(f"r_start: {r_start}. r_end: {r_end}")
            print("Cum sum: ", neg_cumsum_moves[r_end+1]-neg_cumsum_moves[r_start])
            moves += update * (neg_cumsum_moves[end+1]-neg_cumsum_moves[start] - (r_start)*(r_end-r_start) + (r_start-r_spawn)*(r_end-r_start))

            print("moves: ", moves)
            exit()
        else:
            print("Why here.")
            exit()
            moves += update * (cumsum_moves[end+1]-cumsum_moves[start] - (start)*(end-start) + (start-spawn)*(end-start))

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
        cur_ones = np.array(nums[spawn], dtype=np.int32) # TODO: Why is this faster with spawn that without?

        # Setup cumsums
        cumsum_nums = np.concat([[0], np.cumsum(nums)])
        cumsum_moves = np.concat([[0], np.cumsum(nums*(spawn+1))])
        neg_cumsum_moves = np.concat([[0], np.cumsum(nums[::-1]*(spawn+1))])
        print(f"len: {neg_cumsum_moves}")

        # Handle the start seperately to make the rest of the code implementation simpler. 
        print(f"Before start. nums: {np.array(nums, np.int32)}, cumsum_nums: {cumsum_nums}, cumsum_moves: {cumsum_moves} , neg_cumsum_moves: {neg_cumsum_moves}")
        done, cur_ones, moves, left, right = Solution.handle_start(nums, spawn, left, right, cur_ones, moves, k, maxChanges)
        print(f"After start. cur_ones: {cur_ones}, moves: {moves}, left: {left}, right: {right}")

        if not done:
            rad = 2
            while rad < len(nums):
                # The minimum step size that will overshoot
                min_step_size = max(1, int(np.min(k-cur_ones)/2))
                rad += min_step_size
                # print("min_step_size: ", min_step_size)

                # Left case
                next_left = np.maximum(0, left - min_step_size)
                cur_ones, moves = Solution.update_batched_stats(spawn, left, next_left, cur_ones, moves, k, cumsum_nums, cumsum_moves, neg_cumsum_moves, "left")
                left = next_left
                if self.check_end_condition(cur_ones, moves, k, rad): break

                # print(f"After left. cur_ones: {cur_ones}, moves: {moves}, left: {left}, right: {right}")
                # exit()

                # Right case
                next_right = np.minimum(len(nums)-1, right + min_step_size)
                cur_ones, moves = Solution.update_batched_stats(spawn, right, next_right, cur_ones, moves, k, cumsum_nums, cumsum_moves, neg_cumsum_moves, "right")
                right = next_right
                if self.check_end_condition(cur_ones, moves, k, rad): break

                # print(f"After right. cur_ones: {cur_ones}, moves: {moves}, left: {left}, right: {right}")
                # exit()
        return int(np.min(moves[cur_ones==k]))
# COPY ABOVE

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    # result = sol.minimumMoves([1,1,0,0,0,1,1,0,0,1], k=3, maxChanges=1)
    # answer = 3
    # assert result == answer, f"{result} not equal to {answer}"

    # Test 2
    # result = sol.minimumMoves([0,0,0,0], k=2, maxChanges=3)
    # answer = 4
    # assert result == answer, f"{result} not equal to {answer}" 

    # Test 3
    # result = sol.minimumMoves([0,0], k=1, maxChanges=3)
    # answer = 2
    # assert result == answer, f"{result} not equal to {answer}" 

    # Test 4
    # result = sol.minimumMoves([1,1], k=2, maxChanges=4)
    # answer = 1
    # assert result == answer, f"{result} not equal to {answer}" 

    # Test 5
    f = open("./Leetcode/3086_Minimum_Moves_Hard/example.txt", "r")
    nums = [line.strip() for line in f.readlines()][0]
    nums = [int(num) for num in nums[1:-3].split(",")]
    start = time.time()
    result = sol.minimumMoves(nums, k=3818, maxChanges=55)
    end = time.time()
    print("result: ", result, ". Time (s): ", round(end-start, 2))
    # Laptop: time (s):  137.39
    # Parallel improved PC time (s): 3.63
    answer = 6828536
    assert result == answer, f"Calculated value {result} not equal to answer {answer}"

    # Test 6
    # f = open("./Leetcode/3086_Minimum_Moves_Hard/example2.txt", "r")
    # nums = [line.strip() for line in f.readlines()][0]
    # nums = [int(num) for num in nums[1:-3].split(",")]
    # start = time.time()
    # result = sol.minimumMoves(nums, k=23886, maxChanges=15694)
    # end = time.time()
    # print("result: ", result, ". Time (s): ", round(end-start, 2))
    # # Parallel improved PC time (s): 14.92
    # answer = 33169542
    # assert result == answer, f"Calculated value {result} not equal to answer {answer}" 

    # Test 7
    # f = open("./Leetcode/3086_Minimum_Moves_Hard/example3.txt", "r")
    # nums = [line.strip() for line in f.readlines()][0]
    # nums = [int(num) for num in nums[1:-3].split(",")]
    # start = time.time()
    # result = sol.minimumMoves(nums, k=13017, maxChanges=7423)
    # end = time.time()
    # print("result: ", result, ". Time (s): ", round(end-start, 2))
    # # Parallel improved PC time (s): 4.32
    # answer = 15373116
    # assert result == answer, f"Calculated value {result} not equal to answer {answer}" 

    