import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    all_items = os.listdir(path)
    return all_items

path = "C:\Users\HP Pavilion\Documents\pp2_2024"

print("Directories:")
print(list_directories(path))

print("\nFiles:")
print(list_files(path))

print("\nAll Directories and Files:")
print(list_all(path))
