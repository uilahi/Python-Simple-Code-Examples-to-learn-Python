
def allAnagram(input):
    # empty dictionary which holds subsets
    # of all anagrams together
    dict = {}

    # traverse list of strings
    for i in input:

        # sorted(iterable) method accepts any
        # iterable and rerturns list of items
        # in ascending order
        key = ''.join(sorted(i))

        # now check if key exist in dictionary
        # or not. If yes then simply append the
        # strVal into the list of it's corresponding
        # key. If not then map empty list onto
        # key and then start appending values
        if key in dict.keys():
            dict[key].append(i)
        else:
            dict[key] = []
            dict[key].append(i)

            # traverse dictionary and concatenate values
        # of keys together
    output = ""
    for key, value in dict.items():
        output = output + ' '.join(value) + ' '

    return output
l=["bat", "rat", "tab" , "tar", "bad", "abt"]
print(allAnagram(l))