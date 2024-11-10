"""
Link: https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/?ref=header_outind
Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests in 
the party. Note that entries in register are not in any order.
Example : 

Input: arrl[] = {1, 2, 9, 5, 5}
       exit[] = {4, 5, 12, 9, 12}
First guest in array arrives at 1 and leaves at 4, 
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5.  
"""

def maximumGuests(arrl, exit):
    # Insight 1: We don't care which guest leaves. Therefore we do not have to respect the arrl, exit ordering
    arrl.sort() # 1, 2, 5, 5, 9
    exit.sort() # 4, 5, 9, 12, 12
    # 1, 2, 1, 2, 3, 2, 1, 2, 1, 0

    guests = max_guests = 1
    a_i = 1
    e_i = 0
    while a_i < len(arrl) and e_i < len(exit):
        if arrl[a_i] <= exit[e_i]:
            guests += 1
            a_i += 1
            if guests > max_guests:
                max_guests = guests
        else:
            guests -= 1
            e_i += 1
    return max_guests



if __name__ == "__main__":
    answer = maximumGuests([1, 2, 9, 5, 5], [4, 5, 12, 9, 12])
    assert answer == 3, f"Incorrect answer: {answer}. Expected 3."
