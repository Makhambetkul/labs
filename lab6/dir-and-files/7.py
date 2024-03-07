def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())

source_file = "C:\Users\HP Pavilion\Documents\pp2_2024\lab6\dir-and-files\dir\1.txt"
destination_file = "C:\Users\HP Pavilion\Documents\pp2_2024\lab6\dir-and-files\dir\2.txt"

copy_file(source_file, destination_file)
