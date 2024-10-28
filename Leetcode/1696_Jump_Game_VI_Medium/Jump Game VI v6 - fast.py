# https://leetcode.com/problems/prison-cells-after-n-days/description/?submissionId=1436229229
import numpy as np
class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        cells_to_int = np.full(2**len(cells), -1, dtype=np.int16)
        cells_to_int[int(''.join(map(str, cells)), 2)] = 0
        int_to_cells = np.zeros((2**len(cells), len(cells)), dtype=bool)
        cells =  np.array(cells, bool)
        int_to_cells[0] = cells
        for day in range(1, n+1):
            pre_cells = cells.copy()
            cells[0] = cells[-1] = 0 # This can potentially only be performed once at the start.
            # Skip the first and last cells (they are always zero.)
            for j in range(1, len(cells)-1):
                cells[j] = 1 if pre_cells[j-1]==pre_cells[j+1] else 0
    
            cells_int = int(''.join(map(str, cells)), 2)
            if  cells_to_int[cells_int] > -1:
                # Fastforward the computation using the hashtable
                cycle_len = day - cells_to_int[cells_int]
                remaining_steps = n - day
                steps_left = remaining_steps % cycle_len
                final_i = cells_to_int[cells_int] + steps_left
                cells = int_to_cells[final_i]
                break

            cells_to_int[cells_int] = day
            int_to_cells[day] = np.array(cells, bool)
        return list(cells)
        

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    result = sol.prisonAfterNDays([0,1,0,1,1,0,0,1], 7) 
    answer = [0, 0, 1, 1, 0, 0, 0, 0]
    assert result == answer, f"{result} not equal to {answer}"

    # Test 2
    result = sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) 
    answer = [0,0,1,1,1,1,1,0]
    assert result == answer, f"{result} not equal to {answer}"