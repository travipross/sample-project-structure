from sample_package.sample_subpackage.sample_submodule_a import func_a, func_b

def func_x():
    print("Hello, this is func_x. It runs func_a() from another subpackage.")
    func_a()

def func_y():
    print("Hello, this is func_y. It runs func_b() from another subpackage.")
    func_b()

if __name__ == "__main__":
    print("This module (sample_module_a) was called as the main program by the python interpreter. Running both functions in this module.")

    func_x()
    func_y()
