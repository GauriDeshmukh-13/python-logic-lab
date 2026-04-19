def is_palindrome(s):

    """
    Check if given string is a valid palindrome ignoring non-alphanumeric characters.

    Approach:
    - Use two pointers (left, right)
    - Skip non-alphanumeric characters
    - Compare characters after converting to lowercase

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    left, right = 0, len(s)-1

    while left < right:

        #Skip non-alphanumeric characters
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        #Compare characters
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

#Test Cases
if __name__ == "__main__":
    print(is_palindrome("a man, a plan, a canal: Panama")) #True
    print(is_palindrome("race a car"))  #False