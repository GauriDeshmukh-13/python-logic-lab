''' Flatten the List
Write a function to flatten a list that is only one level deep (no recursion needed).
Input: [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5] '''


#Method 1: using extend()
def flatten1(lst):

    output = []

    for n in lst:
        output.extend(n)

    return output

#Method 2: using nested loop
def flatten2(lst2):

    output2 = []

    for sublist in lst2:
        for n in sublist:
            output2.append(n)

    return output2

#Method 3: using List comprehension
def flatten3(lst3):
    #"For each sublist in lst3, then for each n in that sublist, add n to the new list."
    return [n for sublist in lst3 for n in sublist]

if __name__ == "__main__":
    print("Method 1 output: ", flatten1([[1,2],[3,4],[5]]))
    print("Method 2 output: ", flatten2([[1, 2], [3, 4], [5]]))
    print("Method 3 output: ", flatten3([[1, 2], [3, 4], [5]]))