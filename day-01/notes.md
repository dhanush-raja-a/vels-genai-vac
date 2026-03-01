# 🚀 Jupyter Notebook Setup in VS Code (Beginner Guide)

This guide explains how to:
- Install Python
- Install VS Code
- Setup Jupyter Notebook
- Start coding
- Teach beginners effectively

---

## 📌 1. Introduction

### 🐍 What is Python?
- **Python** is a versatile programming language.
- Used in **AI, Web Development, Automation, and Data Science**.
- **Beginner-friendly**: Known for its simple and readable syntax.

### 🧑‍💻 What is VS Code?
- **VS Code (Visual Studio Code)** is a powerful code editor.
- Used to write, debug, and manage code.
- Think of it as **MS Word, but for programming**.

### 📓 What is Jupyter Notebook?
- An **interactive coding environment**.
- Allows you to write code and see the output **instantly**.
- Widely used in **Data Science & AI**.
- **File extension**: `.ipynb`

---

## 🛠 2. Required Installations

### ✅ Step 1: Install Python
1. Visit: [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest version.
3. **During installation:**
    - [ ] ✔ **Tick "Add Python to PATH"** (CRITICAL!)
4. Click **Install Now**.

#### 🔎 Verify Installation
Open your terminal (Command Prompt or Terminal) and type:
```bash
python --version
# OR
python3 --version
```
> If a version number appears, Python is installed successfully!

---

### ✅ Step 2: Install VS Code
1. Visit: [code.visualstudio.com](https://code.visualstudio.com/)
2. Download and install for your OS.
3. Open VS Code.

---

### ✅ Step 3: Install Extensions in VS Code
1. Open VS Code.
2. Click the **Extensions** icon (square boxes) on the left sidebar.
3. Search and Install:
    - 🟢 **Python** (by Microsoft)
    - 🟢 **Jupyter** (by Microsoft)

> [!IMPORTANT]
> These two extensions are mandatory for running notebooks in VS Code.

---

### ✅ Step 4: Install Jupyter Package (if required)
If VS Code asks to install the Jupyter kernel, or if you want to be sure, run this in the VS Code terminal:
```bash
pip install notebook
# OR
pip install jupyter
```
*If `pip` is not recognized:*
```bash
python -m pip install notebook
```

---

## ▶ 3. How to Start Jupyter Notebook in VS Code

### 🔹 Method 1: The VS Code Way (Recommended)
1. Open VS Code.
2. Go to **File → New File...**
3. Open the file type selection and search for **Jupyter Notebook**, or simply save a new file as:
   `demo.ipynb`
4. The Notebook interface will open automatically.
5. **Select Kernel**: Click "Select Kernel" in the top right corner and choose your Python version.
6. Start writing code in the cell!

**Example:**
```python
print("Hello Students")
```

### 🔹 Method 2: The Browser Way
In your terminal, type:
```bash
jupyter notebook
```
This will open the Jupyter dashboard in your default web browser.

---

## 📘 4. Notebook Basics

### 🔹 What is a Cell?
- A block where you write code or text.
- Each cell can be **run independently**.

### 🔹 What is a Kernel?
- The "engine" that executes the Python code.
- If the kernel stops, the code won't run.

### 🔹 Python Files vs. Jupyter Notebooks

| Feature | `.py` File | `.ipynb` File |
| :--- | :--- | :--- |
| **Type** | Plain Python file | Interactive Notebook |
| **Execution** | Runs the entire file | Runs cell by cell |
| **Usage** | Production applications | Learning, analysis, and AI |

---

## 📦 5. Installing Python Libraries
To install external tools/libraries, use `pip`:
```bash
pip install numpy
```
**Common libraries to explore:**
- `numpy`: For math and arrays.
- `pandas`: For data tables.
- `matplotlib`: For charts and graphs.

---

## 🧪 6. Beginner Practice Programs

### Program 1: Basic Output
```python
print("My name is Dhanush")
```

### Program 2: Simple Addition
```python
a = 10
b = 20
print(a + b)
```

### Program 3: User Input
```python
name = input("Enter your name: ")
print("Hello", name)
```

---

## ⚠️ 7. Common Errors & Fixes

- **❌ Python Not Recognized**: Reinstall Python and ensure "Add to PATH" is ticked.
- **❌ Wrong Interpreter Selected**: Click the Python version in the bottom-right or top-right of VS Code and select the correct path.
- **❌ pip Not Working**: Use `python -m pip install <library>`.
- **❌ Kernel Not Connecting**: Try restarting the kernel (circular arrow icon) or restarting VS Code.

---

## 🕒 8. Suggested 3-Hour Teaching Plan

| Time | Activity |
| :--- | :--- |
| **0–30 min** | Explain Concepts (What is Python/VS Code/Jupyter) |
| **30–75 min** | Live Installation Demo |
| **75–180 min** | Hands-on Practice & Beginner Programs |

---

## 🎯 Summary
1. **Install Python** (Add to PATH!)
2. **Install VS Code**
3. **Install Extensions** (Python & Jupyter)
4. **Create `.ipynb` file**
5. **Select Kernel & Start Coding!**

Happy Coding! 🚀
