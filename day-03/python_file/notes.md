# 📘 Phase 1: Python & Traditional NLP Mastery

Welcome to the comprehensive guide for **Day 03**! This note covers everything you need to know about Functions, File Handling, REST APIs, and building your own API with FastAPI. 🚀

---

## 🛠 Prerequisites & Installation

Before running the code, ensure you have the required libraries installed.

### 💻 Local Installation (VS Code, PyCharm, etc.)
Run this command in your terminal:
```bash
pip install requests fastapi uvicorn
```

### ☁️ Running on Google Colab
Google Colab comes with many libraries, but you might need to install `fastapi` and `uvicorn`. 
Add this cell at the top of your notebook:
```python
!pip install fastapi uvicorn requests
```
*Note: Since Colab runs on a remote server, simple `uvicorn.run()` won't open a link on your localhost. You would need tools like `ngrok` or `pytunnel` to expose the API.*

---

## 1️⃣ Reusable Code: Functions (`def`) 🧩

Functions help you write code once and use it multiple times.

### 📝 Example Code
```python
def process_text(text):
    """Cleans and prepares text for NLP."""
    return text.strip().lower()

raw_data = "  NLP is Powerful!  "
cleaned = process_text(raw_data)
print(f"Output: {cleaned}")
```

### 📤 Expected Output
```text
Output: nlp is powerful!
```

### 💡 Explanation
- `def`: The keyword used to define a function.
- `process_text`: The name of the function.
- `text`: The input parameter.
- `return`: Sends the result back to where the function was called.

---

## 2️⃣ File Handling: Working with `.txt` Files 📂

Reading and writing files is essential for processing Large Language Datasets.

### 📝 Example Code
```python
# Writing to a file
with open("nlp_notes.txt", "w") as file:
    file.write("Python for NLP is amazing!\nLearning File Handling.")

# Reading from a file
with open("nlp_notes.txt", "r") as file:
    content = file.read()
    print(content)
```

### 📤 Expected Output
```text
Python for NLP is amazing!
Learning File Handling.
```

### 💡 Explanation
- `open(filename, mode)`: Opens the file. `w` = Write, `r` = Read, `a` = Append.
- `with`: A context manager that automatically closes the file for you. ✅

---

## 3️⃣ REST APIs & JSON Parsing 🌐

REST APIs allow your Python script to communicate with other services.

### 📝 Example Code
```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json() # Parsing JSON to Python Dictionary
    print(f"Title: {data['title']}")
```

### 📤 Expected Output
```text
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

### 💡 Explanation
- `requests.get()`: Sends a request to fetch data.
- `.json()`: Converts the raw web data into a Python dictionary.

---

## 🏗 Practical Project: Wikipedia Text Fetcher 📚

This project fetches text from a live API and saves it locally.

### 📝 Project Code
```python
import requests

def save_wiki_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    res = requests.get(url)
    
    if res.status_code == 200:
        summary = res.json()['extract']
        with open(f"{topic}.txt", "w") as f:
            f.write(summary)
        print(f"✅ Saved summary for {topic}!")
    else:
        print("❌ Error fetching data.")

save_wiki_summary("Natural_language_processing")
```

---

## ⚡ Building APIs with FastAPI 🛠️

FastAPI is the modern way to build high-performance APIs.

### 📝 FastAPI Code
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Traditional NLP!"}

@app.get("/predict/{text}")
def predict(text: str):
    return {"input": text, "length": len(text)}

# To run: uvicorn filename:app --reload
```

### 🌐 Swagger Documentation
FastAPI automatically generates documentation for you!
- **URL**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 🔗
- This allows you to test your API directly in the browser!

### 💡 Explanation
- `@app.get("/")`: Defines a GET route.
- `{text}`: A path parameter that accepts dynamic values.
- `uvicorn`: The lightning-fast server that runs your FastAPI app.

---

## 🎓 Summary Table

| Concept | Python Tool | NLP Use Case |
| :--- | :--- | :--- |
| **Functions** | `def` | Preprocessing pipelines |
| **File Handling** | `open()` | Loading datasets / Saving logs |
| **APIs** | `requests` | Fetching live data for training |
| **JSON** | `json` | Storing structured text data |
| **FastAPI** | `fastapi` | Deploying your NLP models as a service |

✨ **Keep coding and exploring the world of AI & NLP!** ✨
