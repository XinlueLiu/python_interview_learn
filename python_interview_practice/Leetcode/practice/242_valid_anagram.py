# given two strings s and t, return true if t is an anagram of s, and false otherwise
# anagram have same characters and same occurances of characters
# create two dictionary that key being the character, value being number of occurances
# compare the two dictioanry
# or only maintain 1 dictionary. loop through t and decrement number of occurances for each item in dictioanry 1
# dict_s should be empty if anagram


def find_anagram(s,t):
    dict_s = {}
    for each_c in s:
        if (each_c not in dict_s):
            dict_s[each_c] = 1
        else:
            dict_s[each_c] += 1
    for each_c in t:
        if (each_c not in dict_s):
            return False
        else:
            if (dict_s[each_c] == 1):
                dict_s.pop(each_c)
            else:
                dict_s[each_c] -= 1
    # if length is 0, means anagram
    return (len(dict_s) == 0)

s = "anagram"
t = "nagaram"
sol = find_anagram(s,t)
print(sol)


#TODO: dict can pop key using pop(key)
# watch out the condition for key NOT IN dict, may return keyerror