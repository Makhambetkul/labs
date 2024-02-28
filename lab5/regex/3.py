import re
word=input()
print(re.findall("[a-z]+_[a-z]+", word))