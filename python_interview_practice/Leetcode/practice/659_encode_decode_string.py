# design an algorithm to encode a list of strings to a string
# the encoded string is sent to network and decoded back to the origina list of strings

def encoded(plain_text):
    # num#. num is number of characters
    res = ""
    for each_val in plain_text:
        res += str(len(each_val)) + "#" + each_val
    return res

def decoded(strs):
    # pointer(i) that point to the beginning of teach text
    # another pointer(j) checks the length UNTIL # sign(because length may be more than 1 characters)
    # 4#test6$python
    res = []
    i = 0
    # while index i is smaller than the string
    while i < len(strs):
        # two pointers. j pointes to actual characters for each word, i pointes to the beginning of each word
        j = i
        while(strs[j] != "#"):
            # get the leading numerical value that indicates the length
            j += 1
        # excluding the last j element, which is # sign
        # start from next variable of # to the end of the strs(j+1+length will point to next word but [] exclude end pointer)
        length = int(strs[i:j])
        # j + 1 + length because j + length pointes to the last element, but this element will not be included in the string slicing
        res.append(strs[j+1:j+1+length])
        # update i to be beginning of next word, j+1+length
        i = j + 1 + length
    return res


plain_text = ["test", "python"]
cypertext = encoded(plain_text)
print(cypertext)
decoded_text = decoded(cypertext)
print(decoded_text)

# TODO: 1. careful about encode. encode the length of EACH STRING
# 2. need two pointers. one for pointing at each word, one for find length(may be multiple digits)
# 3. loop through the cypertext until i pointes out of the range
# 4. string slicing. END will not be included. j will point to # sign so word is [j+1:j+1+length]
# 5. update i to be the beginning of next word