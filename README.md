# Sample Project Structure

This is a basic project structure to demonstrate some common packaging conventions. Proper packaging isn't required to run Python scripts, but it helps make the code more readable, reusable, and debuggable.

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