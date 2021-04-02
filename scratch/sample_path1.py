import os
import sys

print(f"My directory: {os.getcwd()}")

# file path generated from working directory
fp1 = os.path.join(os.getcwd(), "subfolder1", "test.txt")
print(f"My new filepath: {fp1}")

# file path generated from module location
print(f"my python module: {__file__}")
parent_dir = os.path.dirname(__file__)
print(f"My parent directory: {parent_dir}")
fp2 = os.path.join(parent_dir, "subfolder1", "test.txt")
print(f"My filepath(2): {fp2}")

# Read the file to prove the path is correct
with open(fp1) as sample_file:
    x = sample_file.read()
print(f"File contents: {x}")

print("\n\n\n---------------------------------")


# Build path from command line arguments

# CLI Arguments can be read in a few common ways
# 1. sys.argv -- simpler, but more limited
# 2. argparse -- more feature-rich, slightly more complex

# 1. sys.argv

# print(f"My sys.argv: {sys.argv}")
# fp3 = sys.argv[1]
# print(f"My filepath3: {fp3}")


# 2. argparse
from argparse import ArgumentParser

# define parser
parser = ArgumentParser(description="My first argument parser")
parser.add_argument("-f", "--filepath", type=str, required=True, help="A filepath to a text file")


# read in arguments from command line
args = parser.parse_args()
print(f"My filepath: {args.filepath}")

