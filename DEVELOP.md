# Dev setup

## Installation
Setup an enviroment with either conda or virtualenv
```
conda create -n reactor python=3.11 -y
conda activate reactor
```
```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt

pip install -e . # local editable installation for package
```
