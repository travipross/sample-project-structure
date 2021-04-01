
# Functions to create
# 
# 1. Scan a directory for files
# 2. Open a specific file based on some known properties (by filename format)
# 3. Combine multiple files into continous data series
# 4. Compute basic statistics
# 5. Save statistics

import numpy
import sample_import
import re
from datetime import datetime

DEFAULT_PATTERN = "pfluc_([0-9]{4}[A-Z][a-z]{2}[0-9]{2})_([0-9]+)Hz_([0-9]+)Mics_SC([0-9]{2})_ctrl(Y|N)_([A-Za-z]{2})([0-9]+)Hz_Mod(Y|N)([0-9]{4})Hz_5Vpp_bn([0-9]{4}).npz"


def parse_filename(filename, pattern=DEFAULT_PATTERN):
    """extracts info from filename based on pattern"""
    raw_output = re.match(pattern, filename)

    output_dict = {
        "filename": filename,
        "date": datetime.strptime(raw_output.group(1), "%Y%b%d"),
        "freq": int(raw_output.group(2))
    }

    return output_dict


if __name__ == "__main__":
    print("hello")
    # sample_import.delete_all_my_files()

    test_string1 = "pfluc_2021Mar11_19952Hz_89Mics_SC00_ctrlN_NA50Hz_ModN0000Hz_5Vpp_bn0001.npz"
    test_string2 = "pfluc_2021Mar11_19952Hz_89Mics_SC05_ctrlY_Sn1000Hz_ModY0000Hz_5Vpp_bn0029.npz"
    test_string_combined = f"{test_string1}\n{test_string2}"
    
    # print(f"Test string combined: {test_string_combined}")


    match_dict = parse_filename(test_string1)

    print(match_dict)