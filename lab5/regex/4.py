import re
word=input()
print(re.findall("[A-Z][a-z]+", word))