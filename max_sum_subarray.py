def max_sum_subarray(nums, k):

    """
    Find the maximum sum of subarray of size k

    Approach:
    - Use sliding window of fixed size k
    - Compute initial window sum
    - Slide window by removing left elemwnt and adding right

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    #Initial window sum
    current_sum = sum(nums[:k])
    max_sum = current_sum

    left = 0

    #Slide window
    for right in range(k, len(nums)):
        current_sum = current_sum - nums[left] + nums[right]
        left += 1

        max_sum = max(max_sum, current_sum)

    return max_sum

#Test Case
if __name__ == "__main__":
    print(max_sum_subarray([2,1,5,1,3,2], 3))