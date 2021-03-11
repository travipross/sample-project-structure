from sample_package import EXAMPLE_CONSTANT
## Example: this import comes from the __init__.py file of the python package called sample_package.

def func_a():
    print("Hello, this is func_a.")

def func_b():
    print("Hello, this is func_b.")

if __name__ == "__main__":
    print("This module (sample_submodule_a) was called as the main program by the python interpreter. Running both functions in this module.")

    func_a()
    func_b()

    print(f"EXAMPLE CONSTANT: {EXAMPLE_CONSTANT}")