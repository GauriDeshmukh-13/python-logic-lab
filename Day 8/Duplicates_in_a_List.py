''' Find duplicates in a list
Given a list of integers, return a list of all elements that appear more than once. Order doesn't matter.
Input: [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2]  '''

def duplicates(lst):

    count_dupes = {}
    output = []

    for n in lst:

        if n not in count_dupes:
            count_dupes[n] = 1
        else:
            count_dupes[n] += 1

    for n in count_dupes:
        if count_dupes[n] > 1:
            output.append(n)

    return output

if __name__ == "__main__":
    print(duplicates([1,2,3,2,4,1,5]))