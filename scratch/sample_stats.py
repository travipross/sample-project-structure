from numpy.random import sample
import pandas as pd
import numpy as np


def compute_stats(df):
    stats = {
        "std_dev": df.std().values,
        "skewness": df.skew().values,
        "kurtosis": df.kurtosis().values
    }

    return stats


d1 = {
    "name": "travis",
    "age": 30
}

d2 = {
    "name": "bonnie"
}


# for d in [d1, d2]:
#     print(f"name: {d['name']}, age: {d['age']}")

for d in [d1, d2]:
    print(f"name: {d.get('name')}, age: {d.get('age', 18)}")

if __name__ == "__main__":
    # sample_df = pd.DataFrame(np.random.randint(0, 255, size=(100, 15)))
    sample_df = pd.read_csv("sample_data.txt", sep="\t", header=None) 
    print(sample_df)
    sample_stats = compute_stats(sample_df)

    print(sample_stats)
    