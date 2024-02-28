import re
word=input()
print(re.findall("a.*b$", word))