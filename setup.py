from setuptools import setup, find_packages

# This file is used when "installing" your custom python code. 
# It's not needed if you only intend to run your scripts by providing their filepath to the python interpreter. (e.g. `python my_file.py`).
# It can be helpful to package your projects this way so that they can easily be installed and imported into other environments and projects.


setup(
    name="sample-package",      # Can be any name; this would be how the package appears to the package manager. Should be similar to top-level folder name
    version="0.0.1",            # Good habit to specify a version to keep track of breaking changes in the future, especially if publishing this package
    packages=find_packages(),   # Easy way for (sub)packages to be automatically discovered, but this can be a list of package names
    install_requires=[          # list of requirements for this python library/package to run
        "pandas"
    ]
)
