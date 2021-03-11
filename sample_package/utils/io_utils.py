import pandas as pd 
import os 


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



if __name__ == "__main__":
    # this module is likely only going to be used via importing in other modules, but this block can serve as a test or example
    path_to_top_level_dir = PACKAGE_DIRECTORY
    path_to_sample_csv = os.path.join(path_to_top_level_dir, 'resources', 'sample_data.csv') # rebuilds new path using list of elements


    print(f"Path to open: {path_to_sample_csv}")  # This syntax for formatting variables inside of strings is referred to as 'f-strings'
    df = read_csv(path_to_sample_csv, index_col=0)

    print(df)
