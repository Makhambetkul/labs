def camel_to_snake(camel_case_str):
    snake_case_str = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case_str]).lstrip('_')
    return snake_case_str

camel_str = input()
print(camel_to_snake(camel_str))
