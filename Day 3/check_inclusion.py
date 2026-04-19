def check_inclusion(s1, s2):

    """
    Problem: Permutation in string

    Given two strings s1 and s2, return True if s2 contains any permutations of s1
    Otherwise, return False

    Approach:
    - Use fixed window of size len(s1)
    - Maintain frequency maps for s1 and current window in s2
    - Expand window from right
    - Shrink window from left when size of the window exceeds len(s1)
    - Compare both maps

    Time Complexity: O(n)
    Space Complexity: O(1)

    """
    if len(s1) > len(s2):
        return False

    count_s1 = {}
    count_s2 = {}

    for ch in s1:
        count_s1[ch] = count_s1.get(ch, 0) + 1

    left = 0

    for right in range(len(s2)):

        count_s2[s2[right]] = count_s2.get(s2[right], 0) + 1

        if right - left + 1 > len(s1):
            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]
            left += 1

        if count_s1 == count_s2:
            return True

    return False

if __name__ == "__main__":
    print(check_inclusion("ab", "poubare"))     #True
    print(check_inclusion("aa", "gauri"))       #False
    print(check_inclusion("abc", "because"))    #False