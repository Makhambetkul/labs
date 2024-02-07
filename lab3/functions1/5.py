import itertools

def print_permutations(string):
    permutations = list(itertools.permutations(string))
    for perm in permutations:
        print(''.join(perm))

user_input = input("")
print_permutations(user_input)
