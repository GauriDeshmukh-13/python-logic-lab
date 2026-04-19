def longest_substring(s,k):

    """
    Problem:
    Find maximum length of a longest substring with at most k distinct characters.

    Approach:
    - Use sliding Window (two pointers)
    - Track character frequency using hashmap
    - Shrink window if distinct_chars > k
    - Update maximum length at each valid window

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    left = 0
    distinct_chars  = 0
    count = {}
    max_length = 0

    for right in range(len(s)):

        if s[right] not in count:
            distinct_chars += 1

        count[s[right]] = count.get(s[right], 0) + 1

        #Shrink Window
        while distinct_chars > k:
            count[s[left]] -= 1

            if count[s[left]] == 0:
                del count[s[left]]
                distinct_chars -= 1

            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

#Test Cases
if __name__ == "__main__":
    print(longest_substring("eceba", 2))    #3
    print(longest_substring("abcde", 5))    #5
    print(longest_substring("abcde", 0))    #0
    print(longest_substring("aabbcc", 10))  #6
    print(longest_substring("a", 1))        #1
