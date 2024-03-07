import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")

file_path = "C:\Users\HP Pavilion\Documents\pp2_2024\lab6\dir-and-files\dir\3.txt"
delete_file(file_path)