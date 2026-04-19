def is_anagram(s1, s2):

    """
    Check if strings are valid anagrams.

    Two strings are anagrams if they contain the same characters with the same frequency,
    ignoring spaces and case.

    Approach:
    - Normalize both strings (remove spaces + convert to lowercase)
    - Sort both strings
    - Compare

    Time Complexity: O(n log n) -> due to sorting
    Space Complexity: O(n)
    """

    #Normalize strings
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    #Length check
    if len(s1) != len(s2):
        return False

    #Sort and compare
    return sorted(s1) == sorted(s2)

#Test Cases
if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  #True
    print(is_anagram("Bad Credit", "Debit Card"))  #True
    print(is_anagram("Goodbye", "Good Day")) #False