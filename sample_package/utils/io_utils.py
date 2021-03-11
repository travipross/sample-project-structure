import pandas as pd 
import os 
import glob

# Defining this constant for importing elsewhere
PACKAGE_DIRECTORY = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


def read_csv(path, index_col=None):
    # Convert file path to work between different OS's (windows uses dumb backslashes so this helps correct for that)
    fullpath = os.path.abspath(path)

    # Read dataframe from CSV using whatever loading rules needed. Index col used here as an example.
    df = pd.read_csv(path, index_col=index_col)
    return df


def find_csv_files(search_dir, recursive=False):
    """Finds CSV files in a directory. Setting recursive to True will also search subdirectories"""

    # Raise error if not a valid directory.
    if not os.path.isdir(search_dir):
        raise FileNotFoundError(f"Not a valid directory: {search_dir}")
    
    # The glob tool requires a special "**" wildcard syntax if used in recursive mode to search subdirs, so the
    # base path needs to be constructed differently if so.
    if recursive:
        # using os.path.join to join paths, even though you could just modify the string. The downfall of the latter
        # is that Windows uses backslashes (\) for directory separation, as opposed to basically all other OSes using 
        # forward slashes (/). By using the os.path.join function, the path can be generated dynamically based on the 
        # system running the code.  
        basepath=os.path.join(search_dir, "**")  
    else:
        basepath=search_dir

    # Glob is part of the standard library. This is one of many ways to search a directory for specific patterns, but 
    # I personally find it to be one of the easier approaches. Alternatives include os.scandir and os.walk.
    files = glob.glob(os.path.join(basepath, "*.[cC][sS][vV]"), recursive=recursive)
    return files


if __name__ == "__main__":
    # this module is likely only going to be used via importing in other modules, but this block can serve as a place 
    # for test or example code to be written.
    path_to_top_level_dir = PACKAGE_DIRECTORY
    path_to_sample_csv = os.path.join(path_to_top_level_dir, 'resources', 'sample_data.csv') # rebuilds new path using list of elements


    print(f"Path to open: {path_to_sample_csv}")  # This syntax for formatting variables inside of strings is referred to as 'f-strings'
    df = read_csv(path_to_sample_csv, index_col=0)

    print(df)
