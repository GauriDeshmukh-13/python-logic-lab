def longest_consecutive(nums):

    """
    Find the length of the longest consecutive sequence in an unsorted list.

    Approach:
    -Convert list to set O(1) lookup.
    -Only start counting when the number is the beginning of a sequence
    -Expand forward to count sequence length

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num_set = set(nums)
    max_length = 0

    for num in num_set:

        #Start only when (num-1) not present
        if num-1 not in num_set:
            current = num
            length = 1

            #Expand the sequence
            while current+1 in num_set:
                current+=1
                length+=1

            #Update maximum length
            max_length = max(max_length, length)

    return max_length

#Test Case
if __name__ == "__main__":
    print(longest_consecutive([100,4,200,1,3,2]))

