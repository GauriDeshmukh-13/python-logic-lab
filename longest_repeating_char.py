def longest_repeating_char(s, k):

    """
    Find the length of the longest substring where you can replace at most
    k characters to make all characters the same.

    Approach:
    - Sliding window + frequency map
    - Track mos frequent character in window
    - Shrink window if replacements needed > k

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    count = {}
    max_frequency = 0
    max_length = 0

    for right in range(len(s)):

        #add character
        count[s[right]] = count.get(s[right], 0) + 1

        #update max frequency
        max_frequency = max(max_frequency, count[s[right]])

        #shrink window if invalid
        while (right - left + 1) - max_frequency > k:
            count[s[left]] -= 1
            left += 1

            max_length = max(max_length, right - left + 1)

    return max_length

#Test Cases
if __name__ == "__main__":
    print(longest_repeating_char("AABABAB", 1)) #4
    print(longest_repeating_char("ABAB", 1))    #3
    print(longest_repeating_char("AAAA", 2))    #0