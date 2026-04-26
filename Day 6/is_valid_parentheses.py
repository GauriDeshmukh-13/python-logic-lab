def is_valid_parentheses(s):

    """
    Check if the given string has valid parentheses.

    Approach:
    - Use a stack
    - Push opening brackets
    - On closing bracket, check if it matches top of stack

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    stack = []

    mapping = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for ch in s:

        if ch in mapping.values():
            stack.append(ch)

        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            else:
                stack.pop()

    return len(stack) == 0

#Test Cases
if __name__ == "__main__":
    print(is_valid_parentheses("([()])"))   #True
    print(is_valid_parentheses("()[]{}"))   #True
    print(is_valid_parentheses("([)]"))     #False
    print(is_valid_parentheses(""))         #True
