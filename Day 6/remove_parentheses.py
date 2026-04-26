def remove_parentheses(s):

    """
    Remove Outermost Parentheses

    Approach:
    - Use depth counter to track nesting level
    - If '(' and depth > 0, append it to the result and increase depth
    - If ')' then decrease depth and if depth > 0, add it to the result
    - Join and return the result

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    depth = 0
    result = []

    for ch in s:

        if ch == '(':
            if depth > 0:
                result.append(ch)
            depth += 1

        elif ch == ')':
            depth -= 1
            if depth > 0:
                result.append(ch)

    return "".join(result)

if __name__ == "__main__":
    print(remove_parentheses("(())"))       #()
    print(remove_parentheses("(())(())"))   #()()
    print(remove_parentheses("()()"))       #empty
