# Data-Extractor
Tool for extracting xy data from an image. Handy for grabbing data from old science papers.

## Install with UV
Install uv with the standalone installer, run this command in any terminal window:
```
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Now, open a terminal at the root of this project, and run this command to create a virtual environment and install dependencies.
```
uv sync
```


And that should be all good to go! try running the program directly with
```
uv run ./src/main.py
```

Export setting to requirements file:
```
uv pip compile pyproject.toml > requirements.txt
```

## Install with PIP
Install the python version recorded in this [file](.python-version).
It is strongly recommended to create a new virtual environment for each new project.


Run the commend below in a terminal at the root of this project.
```
py -3.12 -m venv .venv
```

Activate the new environment:
```
.venv/scripts/activate
```

Install packages from requirements file:
```
pip install -r requirements.txt
```