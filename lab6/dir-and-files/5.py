def write_list_to_file(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')

my_list = [1, 2, 3, 4, 5]
filename = "1.txt"
write_list_to_file(filename, my_list)
