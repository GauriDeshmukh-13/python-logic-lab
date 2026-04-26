def check_subarray_sum(nums, k):

    """
    Problem:
    Check if there exists a continuous subarray of size >= 2
    whose sum is a multiple of k.

    Approach:
    - Use prefix sum and a hashmap to track remainders.
    - Compute running sum and take remainder = current_sum % k.
    - If the same remainder is seen again, it means the subarray
      between indices has sum divisible by k.
    - Store remainder with its first occurrence index.
    - Ensure subarray length is at least 2 (i - prev_index >= 2).

    Edge Cases:
    - If k == 0, check if there exists a subarray with sum = 0.
    - Works with negative numbers as well.
    """
    current_sum = 0
    remainder_map = {0:-1}

    for i in range(len(nums)):
        current_sum += nums[i]

        if k != 0:
            remainder = current_sum % k
        else:
            remainder = current_sum

        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i

    return False

if __name__ == "__main__":
    print(check_subarray_sum([5,0,0], 5))           #True
    print(check_subarray_sum([1,2,3], 5))           #True
    print(check_subarray_sum([1,2,3], 0))           #False
    print(check_subarray_sum([-1,-2,-3, 4, 0], -2))    #True

