
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    # push the two strings to tw dictionaries
    # key is string character, value is character occurances
    # if the two dictionaries are equal, then anagram
    dict1 = {}
    dict2 = {}
    for val in s:
        if (val in dict1):
            dict1[val] += 1
        else:
            dict1[val] = 1
    for val in t:
        if (val in dict2):
            dict2[val] += 1
        else:
            dict2[val] = 1
    if (dict1 == dict2):
        print("True")
    else:
        print("False")