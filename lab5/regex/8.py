import re

def split_string(input_string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', input_string).split('_')

input_string = input()
result = split_string(input_string)
print(result)