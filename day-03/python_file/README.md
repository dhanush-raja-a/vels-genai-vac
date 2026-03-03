# Day 03: Python & Traditional NLP Basics

Welcome to Day 03! Today we cover essential Python skills for NLP, including functions, file handling, and interacting with web APIs.

## Folder Structure
- `requirements.txt`: List of dependencies (install via `pip install -r requirements.txt`).
- `01_functions.py`: Learn how to write reusable code block using `def`.
- `functions_guide.ipynb`: **(New)** In-depth interactive guide on functions.
- `sample.txt`: A sample text file used for reading exercises.
- `02_file_handling.py`: Learn how to read and write `.txt` files.
- `03_rest_apis_json.py`: Learn how to fetch data from APIs and parse JSON.
- `04_wikipedia_project.py`: A project that combines everything! Fetches a Wikipedia page and saves it to a file.
- `05_fastapi_tutorial.py`: **(New)** Learn how to build your own API using FastAPI.

## How to use these files:
1. Open your terminal in this folder.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the files in order:
   - `python 01_functions.py`
   - `python 02_file_handling.py`
   - `python 03_rest_apis_json.py`
   - `python 04_wikipedia_project.py`
   - `python 05_fastapi_tutorial.py` (Starts a local server at `http://127.0.0.1:8000`)

### FastAPI Documentation
When running `05_fastapi_tutorial.py`, you can access the interactive Swagger documentation here:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Topics Covered:
- **Reusable code (def)**: Organizing logic into functions.
- **File Handling**: Reading `.txt` files and writing output.
- **REST APIs**: Using `requests` to fetch live data.
- **JSON parsing**: Working with structured data from APIs.
