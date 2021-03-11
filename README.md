# Sample Project Structure

This is a basic project structure to demonstrate some common packaging conventions. Proper packaging isn't required to run Python scripts, but it helps make the code more readable, reusable, and debuggable.

## Note about `pip` and `conda`
Most "general" python package management is done via `pip`. Its sole responsibility is to be a package manager. It is used to install and uninstall different python dependencies (python libraries/packages). Some python packages depend on compiled dependencies (binaries) and other non-python libraries. Depending on your CPU architecture and installed python version, pre-built binaries may be available when running `pip install`. When they are not, a `C/C++` compiler may be required on the system in order to build and install the dependencies for a python package. On Windows OS, this can be a bit of a pain.

In the field of data science `conda` is more commonly seen. It is both a package manager and and environment manager (more on that later) in one. One thing that sets `conda` aside from `pip` is that it can also manage non-python packages. There are fewer packages publicly available when using `conda` as compared to `pip`, but `conda` may be seen as an easier tool to use, especially on Windows where non-python dependencies may otherwise require a `C/C++` compiler. 

Though `pip` can be used to install packages alongside those installed by `conda`, there is some risk of dependency conflicts arising. Combining of these tools should be done sparingly, if ever.


## Virtual Environments
In recent versions of `python3` (`3.3+`), the `venv` tool is shipped as part of the standard library. It can be used to create "virtual environments". This allows you to have different versions of python dependencies concurrently installed on the same machine for different projects. It provides isolation and repeatability. It is good practice to develop in a virtual environment, so as to not interfere with system-level depenedencies that may be already installed.

To create a new virtual environment, run the following command:
```
python -m venv /path/to/venv
```

To activate the virtual environment, run the following command: 
```
source /path/to/venv/bin/activate     # on linux/macOS
```
or
```
/path/to/venv/Scripts/activate.bat    # on windows
```

Once activated, you can freely install, upgrade, or uninstall python packages as you wish, without fear of breaking any system-level packages, or interfering with any other virtual environment created.

### Note about conda
Conda has a similar concept of virtual environments of its own. You should avoid mixing these two concepts. As a rule of thumb, if using `conda` to install packages, also use `conda` to manage environments.

To create an environment in `conda`, run the following:
```
conda create --name myenv
```

To activate that environment, run:
```
conda activate myenv
```

See [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more information.

## Installing
You can *optionally* install this project by navigating to the top level directory in a terminal, and running
```
pip install .
```

... Or you can install in "editable" mode by running
```
pip install -e .
```
Editable mode means that you don't need to reinstall when you make changes to the source code; they will be reflected in the environment automatically.

The `setup.py` file in the top level directory defines how the package is installed. This file calls the `setup()` function from the `setuptools` package, and passes a number of arguments to define dependencies, and metadata about this package. When package managers (like `pip`) are directed to "install" a package from a local directory, they look for this `setup.py` file adjacent to the package/library directory (not inside it).
```
../sample-project-structure
├── README.md
├── resources
│   └── sample_data.csv
├── sample_package
│   ├── __init__.py
│   ├── sample_module_a.py
│   ├── sample_subpackage
│   │   ├── __init__.py
│   │   └── sample_submodule_a.py
│   └── utils
│       ├── __init__.py
│       └── io_utils.py
└── setup.py
```


## Running Code

### When Installed
If installed in the local python environment, modules can be executed by providing the `-m` flag to the interpreter, and then a '`.`' separated  path to the module (**Note:** No file extension is provided, as it is not a filesystem path).
```
python -m sample_package.sample_subpackage.sample_submodule_a
```

### When Not Installed
If this package isn't "installed", the code can still be executed by providing the full path of a script to the interpreter: 
```
python <...>/sample_package/sample_subpackage/sample_submodule_a.py
```