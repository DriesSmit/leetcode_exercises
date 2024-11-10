"""
Given a 2-dimensional integer array arr[] representing N ranges, each of type [starti, endi] (starti, endi ≤ 109) and Q queries represented 
in array query[], the task is to find the maximum occurrence of query[i] (query[i] ≤ 109) in the given ranges for all i in the range [0, Q-1].

Examples:


Input: arr[] = {{1, 5}, {3, 6}, {5, 7}, {12, 15}}, query[] = {1, 3, 5, 13}
Output: {1, 2, 3, 1}
Explanation: The occurrence of 1 in the range is 1.
The occurrence of 3 in the range is 2.
The occurrence of 5 in the range is 3.
The occurrence of 13 in the range is 1.


Input: arr[] = {{2, 5}, {9, 11}, {3, 9}, {15, 20}}, query[] = {3, 9, 16, 55}
Output: {2, 2, 1, 0}
"""
import bisect
from collections import defaultdict
def findMaxOccurence(arr, queries):
    # Time complexity: O(nlog(n))
    # Space complexity: O(n)

    # Hashmap prefix sum
    r_hash = defaultdict(int)
    for (s, e) in arr:
        r_hash[s] += 1
        r_hash[e+1] -= 1

    # Create array and prefix_sum
    nums = list(r_hash.items())
    nums.sort()

    # Create a prefix sum
    val = [nums[0][0]]
    freq = [nums[0][1]]
    for i in range(1, len(nums)):
        (num, delta) = nums[i]
        val.append(num)
        freq.append(freq[i-1]+delta)
    
    outputs = []
    for q in queries:
        # Find the closest match using binary search
        r = bisect.bisect_left(val, q)
        if 0 <= r < len(freq):
            if val[r] != q:
                r -= 1
            if r >= 0:
                outputs.append(freq[r])
            else:
                outputs.append(0)
        else:
            outputs.append(freq[-1])
    return outputs

# def findMaxOccurence(arr, queries):
#     # Time complexity: O(n^2)
#     # Space complexity: O(q)
#     outputs = []
#     for q in queries:
#         count = 0 
#         for (s, e) in arr:
#             if s <= q <= e:
#                 count += 1
#         outputs.append(count)
#     return outputs

if __name__ == "__main__":
    answer = findMaxOccurence([[2, 5], [9, 11], [3, 9], [15, 20]], [3, 9, 16, 55])
    assert answer == [2, 2, 1, 0], f"Incorrect answer: {answer}. Expected [2, 2, 1, 0]."
