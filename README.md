# Data-Extractor
Tool for extracting xy data from an image. Handy for grabbing data from old science papers.

# Install
Install python, the version used should be recorded in this [file](.python-version)


It is strongly recommended to create a new virtual environment for each new project.
Run the commend below in a terminal at the root of this project.

```
py -m venv .venv
```

Activate the new environment:
```
.venv/scripts/activate
```

Install packages from requirements file:
```
pip install -r requirements.txt
```
**Note:** this is limited to the packages directly used in this project. Dependencies for libraries will be resolved by pip.

To install all binaries recorded in the freeze.txt file:
```
pip install -r freeze.txt
```