def group_anagrams(words):

    """
    Group words that are anagrams of each other.

    Approach:
    -Use dictionary where:
        key = sorted version of the word
        value = list of words with same sorted form
    -Words with same sorted characters belong to same group

    Time complexity: O(n * k log k)
        n = number of words
        k = average length of each word (sorting takes k log k )
    Space complexity: O(n*k)
    """

    groups = {}

    for word in words:

        #Create a key by sorting characters of the word
        key = "".join(sorted(word))

        #Initialize list if key is not present
        if key not in groups:
            groups[key] = []

        #Add word to corresponding group
        groups[key].append(word)

    #Rerturn grouped anagrams
    return list(groups.values())

if __name__ == "__main__":
    words = ["eat", "sit", "ate", "its","tap","pat","bat","apt"]
    print(group_anagrams(words))

