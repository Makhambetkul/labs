def count_lines(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The file '{file_path}' has {line_count} line(s).")
    else:
        print(f"File '{file_path}' not found.")


import os
file_path = r"C:\Users\HP Pavilion\Documents\pp2_2024\lab6"
count_lines(file_path)
