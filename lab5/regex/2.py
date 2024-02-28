import re
word=input()
print(re.findall("ab{2,3}", word))