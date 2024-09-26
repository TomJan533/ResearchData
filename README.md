# Research data

Prerequisities:

Download 2 csv files to root of this project:
- recruitment - awards.csv
- recruitment - emails.csv

## Setup

Virtual Environment and dependencies
```bash
python -m  venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Jupyter Notebook

Run Jupyter Notebook
```bash
jupyter notebook
```

Navigate your browser to:
http://127.0.0.1:8888/notebooks/awards-analysis.ipynb

NOTE: remember to clear cells outputs before commit !

## Execute main script

```bash
python main.py
```

Excecuting all steps in Jupyter Notebook or running main script should result with following files
saved to root of this project:

- emails - awards (full).csv
- emails - awards (join check).csv (for debugging purposes)