# For min and max equivalents look at sparse tables.

# function to find cumulative sum of list
from itertools import accumulate 
 
def prefix_sum(lst): 
    return [0] + list(accumulate(lst))
 
# Driver program 
if __name__ == "__main__": 
    lst = [3, 4, 1, 7, 9, 1]
    p_sum = prefix_sum(lst)

    # Sum between index 0 (included) and 2 (excluded) = 7
    print(p_sum[4]-p_sum[0])