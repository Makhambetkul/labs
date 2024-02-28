import re
word=input()
def space(word):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', word)
result=space(word)
print(result)