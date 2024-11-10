"""
Link: https://www.geeksforgeeks.org/find-frequency-of-the-elements-in-given-ranges/
Given a 2-dimensional integer array arr[] representing N ranges, each of type [starti, endi] (starti, endi ≤ 109) and Q queries represented in array query[], the task is to find the maximum occurrence of query[i] (query[i] ≤ 109) in the given ranges for all i in the range [0, Q-1].

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

# Python3 code to implement the approach
import bisect
 
# Function to find the frequency
# of element in array arr
def findTheOccurrence(arr, q, result):
    n = len(arr)
     
    # Map to store the elements
    # with their frequency
    mp = {}
 
    for i in arr:
        if i[0] not in mp:
            mp[i[0]] = 0
        if (i[1] + 1) not in mp:
            mp[i[1] + 1] = 0
        mp[i[0]] += 1
        mp[i[1] + 1] -= 1
         
 
    range = []
    freq = []
    prefixSum = 0
 
    for i in sorted(mp.keys()):
 
        # Calculate the frequency of element
        # using prefix sum technique.
        prefixSum = prefixSum + mp[i]
 
        # Store the element of arr in range
        range.append(i)
 
        # Store its corresponding frequency
        freq.append(prefixSum)
 
     
    # Iterate over the query
    for p in q:
 
        # Find the lower_bound of query p
        idx = bisect.bisect_left(range, p)
 
        # If the lower_bound doesn't exist
        if (idx >= 0 and idx < len(range)):
 
            # Check if element
            # which we are searching
            # exists in the range or not.
            # If it doesn't exist then
            # lower bound will return
            # the next element which is
            # just greater than p
            if (range[idx] != p):
                idx -= 1
            if (idx >= 0):
                result.append(freq[idx])
 
            # If no such element exist
            else:
                result.append(0)
 
        # If idx is range size,
        # it means all elements
        # are smaller than p.
        # So next smaller element will be
        # at range.size() - 1
        else :
            result.append(freq[len(range) - 1])
     
    # Return the final result
    return result
 
 
 
# Driver code
# arr = [[ 1, 5 ], [ 3, 6 ], [ 5, 7 ], [ 12, 15 ] ]
# q = [ 1, 3, 5, 13 ]
arr = [[2, 5], [9, 11], [3, 9], [15, 20]]
q = [3, 9, 16, 55]
result = []
 
# Function call
result = findTheOccurrence(arr, q, result)
 
print(" ".join(list(map(str, result))))