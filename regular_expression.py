#regex is a procesure in any language to look for a specified pattern in a given text
#pattern is a sequence of characters, which represent multiple strings
import re
#how to create pattern
text = "This it a python3 a.p script and __ it Is chongchongchong! a.p"
#so going to search is or it
#[abc] will mathc a or b or c
#pattern = "i[st]"
#pattern = "[a-f]"
#\w, matches any single letter, digit, or underscore. NOT space
#\W(capitalizaed). Any pattern not \w include, including spaceiing
#\d is only digit
#pattern = "\w\w"
#. matches any single character except new line character
#\ symbol is the escape symbol

#^ means start of the string, $ means end of the string
#\b will match empty string at the beginning or end of a word. 
#\B will not match any empty string at the beginning of end of a word
#so if match is, something like this will not be matched
#pattern = "\w\.\w"
#two slashes to escape the \(escape symbol), or use r(raw string) that does not escape
#\t,\n,\r matches tab, newline, return

#{2} means two times. {2,4} means 2,3, or 4 times. {2,} means 2 or more times
#+ means one or more. * means 0 or more times
#? means once or none

#flags
#re.I ignore cases(case insensitive)
#re.M will look multiline
#if want multiple flags, re.M|re.I. |this is the pipe symbol
text2 = """this
is
a
multiline
string"""
#print(text)
#search will only return the first match. If no match, will return None
#and it will look at the entire string(including multiline)
#match will only look for one line. Even re.M won't work. And it will look at the beginning of the line
pattern = r"i[st]"
#this will also be matched. ONLY MATCH STRING
print(len(re.findall(pattern, text)))
#print(re.findall(pattern, text,re.I))
match_ob = re.search(pattern, text)
if match_ob:
    print(match_ob)
    print(f'matched the pattern "{match_ob.group()}"')
    print(f'starting index is "{match_ob.start()}"')
    print(f'ending index is  "{match_ob.end() - 1}"')
    print(f'length of matched object "{match_ob.end() - match_ob.start()}"')
    #print(re.findall("is",text))
else:
    print("no match found")

for each_ob in re.finditer(pattern, text):
    #and the start, end are the same as search
    print(f'matched for finditer "{each_ob.group()}"')

new_text = "this is about python script, and I wish I know necessary Python scripting"
new_pattern = "python"
print(re.split(new_pattern, new_text, flags=re.I))
#can use re.maxsplits to consider maximum splits. if less than all splits, it goes left to right
#can use re.sub to change the string and store it elsewhere. The 
#original string won't change
#subn will also return number of places you replaced

#compile changes a pattern into an obkect, which can then be used for matching
#using match(), search(), and other methods, or flags