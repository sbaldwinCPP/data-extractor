# Data-Extractor
Tool for extracting xy data from an image. Handy for grabbing data from old science papers.

# Install
Install python, version 3.11 was used and should be recorded in this [file](.python-version)


It is strongly recommended to create a new virtual environment for each new project.


Run the commend below in a terminal at the root of this project.
```
py -3.11 -m venv .venv
```

Activate the new environment:
```
.venv/scripts/activate
```

Install packages from requirements file:
```
pip install -r requirements.txt
```
**Note:** this is limited to the packages directly used in this project. Dependencies for libraries will be resolved by pip. The requirements.txt file needs to be maintained by hand, pip does not keep track of which binaries are actually imported to the project, and which are just dependencies.

To install all binaries recorded in the freeze.txt file:
```
pip install -r freeze.txt
```

Record all binaries:
```
pip freeze > freeze.txt
```