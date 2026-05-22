def string_reversal(s):

    reversed_s = ""

    for ch in s:
        reversed_s = ch + reversed_s

    return reversed_s

if __name__ == "__main__":
    print(string_reversal('abc'))
    print(string_reversal('10100110'))