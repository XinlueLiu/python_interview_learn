
def encode(strs):
    res = ""
    # encode into form length_of_word+#+actual_word
    for n in strs:
        res += str(len(n)) + "#" + n
    return res

def decode(strs):
    # decode by checking is there number followed by # sign
    # if so extract the word with length
    res = []
    i = 0
    while i < len(strs):
        # two pointers. j pointes to actual characters for each word, i pointes to the beginning of each word
        j = i
        while(strs[j] != "#"):
            # get the leading numerical value that indicates the length
            j += 1
        # excluding the last j element, which is # sign
        # start from next variable of # to the end of the strs(j+1+length will point to next word but [] exclude end pointer)
        length = int(strs[i:j])
        res.append(strs[j+1:j+1+length])
        # update i to be beginning of next word, j+1+length
        i = j + 1 + length
    return res

if __name__ == "__main__":
    strs = ["whateveritisaproblem","is","this","problem"]
    encoded_str = encode(strs)
    print(encoded_str)
    decoded_str = decode(encoded_str)
    print(decoded_str)