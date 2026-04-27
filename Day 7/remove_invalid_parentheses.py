def remove_invalid_parentheses(s):

    """
    Problem: Remove minimum number of invalid parentheses to make the string valid.

    Approach:
    1. First Pass: (Left -> Right)
        - Remove extra closing brackets ')'
        - Keep track of open_count.
        - Add ')' only if open_count > 0

    2. Second Pass: (Right -> Left)
        - Remove extra opening brackets '('
        - We know how many extra opening brackets from open_count

    3. Reverse the result to restore correct order

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    open_count = 0
    result = []

    #Pass 1: Remove extra ')'
    for ch in s:
        if ch == '(':
            open_count += 1
            result.append(ch)

        elif ch == ')':
            if open_count > 0:
                open_count -= 1
                result.append(ch)

        else:
            result.append(ch)

    #Pass 2 : remove extra '('
    final = []
    open_to_remove = open_count

    for ch in reversed(result):
        if ch == '(' and open_to_remove > 0:
            open_to_remove -= 1
        else:
            final.append(ch)

    return "".join(reversed(final))


#Test Cases
if __name__ == "__main__":
    print(remove_invalid_parentheses("lee(t(c)o)de)"))      #lee(t(c)o)de
    print(remove_invalid_parentheses("lee(((t(c)o)de)"))    #lee(((tc)o)de)
    print(remove_invalid_parentheses("a)b(c)d"))            #ab(c)d
    print(remove_invalid_parentheses("((a)"))               #(a)