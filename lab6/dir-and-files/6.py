import os

path_to_folder = 'C:\Users\HP Pavilion\Documents\pp2_2024\lab6\dir-and-files\dir'

for i in range(65, 90):
    s=chr(i)
    with open(path_to_folder + f"{s}.txt", "w") as file:
        file.write(f"This is {s}.txt")