# https://leetcode.com/problems/minimum-moves-to-pick-k-ones
from tqdm import tqdm
import time

# COPY BELOW
import sys
class Solution(object):
    @staticmethod
    def num_moves(spawn, nums, k, maxChanges, min_moves):
        """
        :type i: int
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """

        nums = list(nums)
        left, right = 0, 0
        used_max_changes = False
        cur_ones = nums[spawn]
        nums[spawn] = 0
        moves = 0
        while cur_ones < k:
            if not used_max_changes and (left >= 2 or spawn-left==0) and (right >= 2 or spawn+right == len(nums)-1):
                used_max_changes = True
                # Use the maxChanges
                if k-cur_ones >= maxChanges:
                    cur_ones += maxChanges
                    moves += maxChanges*2
                else:
                    moves += 2*(k-cur_ones)
                    # cur_ones = k
                    break

            elif 0 < spawn-left and (left <= right or spawn+right >= len(nums)-1):
                # Increment left
                left += 1
                if nums[spawn-left] == 1:
                    moves += left
                    cur_ones += 1
            else:
                # Increment right
                right += 1
                if nums[spawn+right] == 1:
                    moves += right
                    cur_ones += 1
            
            if cur_ones >= k:
                assert cur_ones == k
                break
                
            if moves >= min_moves:
                # Stop searching. We already have a better solution.
                break

        return moves
    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        min_moves = sys.maxsize
        for i in tqdm(range(len(nums))):
            # TODO: Start the search in a dense area and loop around in necessary

            # Start in the middle as there is on average more values to search from
            j = (i + int(len(nums)/2))%len(nums)

            moves = Solution.num_moves(j, nums, k, maxChanges, min_moves)
            # print(f"i: {i}. moves: {moves}")
            if moves < min_moves:
                min_moves = moves
        return min_moves
# COPY ABOVE

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    # result = sol.minimumMoves([1,1,0,0,0,1,1,0,0,1], 3, 1)
    # answer = 3
    # assert result == answer, f"{result} not equal to {answer}"

    # Test 2
    # result = sol.minimumMoves([0,0,0,0], 2, 3)
    # answer = 4
    # assert result == answer, f"{result} not equal to {answer}" 

    # Test 3
    f = open("./Leetcode/3086_Minimum_Moves_Hard/example.txt", "r")
    nums, k, maxChanges = [line.strip() for line in f.readlines()]
    nums = [int(num) for num in nums[1:-3].split(",")]
    start = time.time()
    result = sol.minimumMoves(nums, int(k), int(maxChanges))
    end = time.time()
    print("result: ", result, ". Time (s): ", round(end-start, 2))
    # Laptop: Time (s):  137.39
    answer = 6828536
    assert result == answer, f"{result} not equal to {answer}" 

    