import os
import sys


def read_and_print(filepath):
    with open(filepath) as f:
        print(f"Filename: {filepath}, contents: {f.read()}")

# assume full path (or relative path from working directory) to folder is provided as CLI arg
file_dir = sys.argv[1]

# list contents
filenames = sorted(os.listdir(file_dir))
print(f"Filenames: {filenames}")

# loop through files, opening and printing each one
for file in filenames:
    read_and_print(os.path.join(file_dir, file))


