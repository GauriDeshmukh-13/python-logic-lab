def subarray_sum(nums, k):

    """
    Problem: Subarray Sum Equals K

    Approach:
    - Use Prefix Sum + HashMap
    - Maintain a running sum (current_sum)
    - At each step, check if (current_sum - k) exists in the hashmap
    - If yes, subarray with sum = k exists
    - Store frequency of prefix sums in hashmaps

    Pattern:
    - Prefix Sum
    - HashMap

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = 0
    prefix_map = {0:1}
    current_sum = 0

    for n in nums:
        current_sum += n

        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]

        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count

if __name__ == "__main__":
    print(subarray_sum([1,1,1], 2))         #2
    print(subarray_sum([3], 3))             #1
    print(subarray_sum([3], 2))             #0
    print(subarray_sum([1, -1, 1, 1], 2))   #2
    print(subarray_sum([1, 2, 3], 100))     #0