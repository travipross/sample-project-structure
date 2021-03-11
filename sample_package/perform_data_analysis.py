from sample_package.utils.io_utils import read_csv, find_csv_files
import sys


# Assert that input arguments were provided; sys.argv will be a list whose elements are command line arguments
# that were provided to the interpreter when launching this script. sys.argv[0] will be the scripts name, and 
# each subsequent element are the arguments provided.
if len(sys.argv) < 2:
    print("No path provided at command line. Please provide a path to a CSV.")
    exit(1)

print("This is an example data analysis module.")


# Assuming a single argument was provided at the command line after the script name, this would be stored in sys.argv[1].
# Here, I assume it's a file path. The next argument would be in sys.argv[2], etc.
#
# There are better approaches to handling input arguments (e.g. argparse, click), but for simple program structures, this
# approach works fine and is more intuitive.
PATH = sys.argv[1]

# An example of using a function defined in another module. This simply searches the provided directory for csv files.
files = find_csv_files(PATH, recursive=True)
print(f"Files found: {len(files)}\n")

# Looping over each file to do something. This uses another custom function imported from elsewhere.
for f in files:
    df = read_csv(f, index_col=0)
    print(f"Data frame for {f}:\n{df}\n")


# Note: this file doesn't have the "if __name__ == '__main__'" block, so if this file is imported by another python process,
# all code will be executed. By wrapping in such a block, you can ensure that any functions defined in this file are importable
# in other files, without this file actually running all the contained code. Example of how this file could look below:

################################################
# def my_main_function(input_path_arg):
#     files = find_csv_files(input_path_arg)
#     for f in files:
#         do_stuff_to_file(f)
#
#
# if __name__ == "__main__":
#     path = sys.argv[1]
#     my_main_function(path)
################################################


# It's generally good practice to do this wherever possible.
