def longest_unique_substring(s):

    """
    Find the length of the longest substring without repeating characters

    Approach:
    - Use sliding window with two pointers (left, right)
    - Maintain a set to track unique characters
    - Expand window using right pointer
    - If duplicate found, shrink window from left

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        #Shrink window if duplicate character found
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        #Add current character to the set
        char_set.add(s[right])

        #Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

#Test Cases
if __name__ == "__main__":
    print(longest_unique_substring("abcabcdbb"))    #4
    print(longest_unique_substring("bbbb"))         #1
    print(longest_unique_substring("aaabbbccc"))    #2
