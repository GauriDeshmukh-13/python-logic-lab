def min_subarray_len(target, nums):

    """
    Find the minimum length of the subarray with sum >= target

    Approach:
    - Sliding window (variable size)
    - Expand window by moving right
    - Shrink window when condition is met

    Time Complexity = O(n)
    Space Complexity = O(1)
    """

    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):

        current_sum += nums[right]

        #shrink window when condition is satisfied
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length==float('inf') else min_length

#Test Cases
if __name__ == "__main__":
    print(min_subarray_len(7, [2,3,1,2,4,3]))   #2
    print(min_subarray_len(4, [0,0,0,0]))       #0
    print(min_subarray_len(20, [1,2,3,4,5,6]))  #5