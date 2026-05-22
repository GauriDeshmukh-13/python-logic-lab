def vowel_count(s):

    vowels = set('aeiou')
    return sum(1 for ch in s.lower() if ch in vowels)

if __name__ == "__main__":
    print(vowel_count("Isometric"))
    print(vowel_count("Hi, I am your aunt."))
    print(vowel_count("AEi0U-"))