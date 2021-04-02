import os
import argparse
import glob

def read_and_print(filepath):
    """Reads a file and prints contents to STDOUT"""
    with open(filepath) as f:
        print(f"Filename: {filepath}, contents: {f.read()}")


def list_text_files_in_dir(dir, recursive=True):
    """ List files ending in .txt"""
    if recursive:
        path_pattern = os.path.join(dir, "**", "*.txt")
    else:
        path_pattern = os.path.join(dir, "*.txt")

    filenames = glob.glob(path_pattern, recursive=recursive)
    return filenames


def main(file_dir):
    # list contents
    filenames = list_text_files_in_dir(file_dir)

    # loop through files, opening and printing each one
    for file in filenames:
        read_and_print(file)

def cli():
    # use argparse to accept a path to a directory
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", required=True, help="Path to directory containing TXT files")
    args = parser.parse_args()

    file_dir = args.dir
    print(f"Directory: {file_dir}")

    main(file_dir)


if __name__ == "__main__":
    cli()
