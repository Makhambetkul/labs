def snake_to_camel(snake):
    words = snake.split('_')
    camel= [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case_str = ''.join(camel)
    return camel_case_str

snake = input()
camel = snake_to_camel(snake)
print(camel)
