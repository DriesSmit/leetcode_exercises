# https://leetcode.com/problems/prison-cells-after-n-days/

class Solution(object):
    @staticmethod
    def prisonAfterNDays(cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        cells_to_int = [-1]*(2**len(cells))
        cells_to_int[int(''.join(map(str, cells)), 2)] = 0
        int_to_cells = [list(cells)]
        for day in xrange(1, n+1):
            pre_cells = list(cells)
            cells[0] = cells[-1] = 0 # This can potentially only be performed once at the start.
            # Skip the first and last cells (they are always zero.)
            for j in xrange(1, len(cells)-1):
                cells[j] = 1 if pre_cells[j-1]==pre_cells[j+1] else 0
    
            cells_int = int(''.join(map(str, cells)), 2)
            if cells_to_int[cells_int] > -1:
                # Fastforward the computation using the hashtable
                steps_left = (n - day) % ( day - cells_to_int[cells_int])
                cells = int_to_cells[cells_to_int[cells_int] + steps_left]
                break

            cells_to_int[cells_int] = day
            int_to_cells.append(list(cells))
        return cells
    
# DO NOT COPY BELOW
# from memory_profiler import memory_usage

# # [22.3515625, 22.3515625, 22.3515625]
# def test_memory():
#     sol = Solution()
#     result = sol.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)
#     answer = [0, 0, 1, 1, 1, 1, 1, 0]
#     assert result == answer, f"{result} not equal to {answer}"

# # Run and measure memory
# mem_usage = memory_usage(test_memory)
# print(f"Memory usage: {mem_usage}")
if __name__ == "__main__":
    sol = Solution()

    # Test 1 (Uncomment to test this case as well)
    result = sol.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7)
    answer = [0, 0, 1, 1, 0, 0, 0, 0]
    assert result == answer, f"{result} not equal to {answer}"

    # Test 2
    result = sol.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)
    answer = [0, 0, 1, 1, 1, 1, 1, 0]
    assert result == answer, f"{result} not equal to {answer}"