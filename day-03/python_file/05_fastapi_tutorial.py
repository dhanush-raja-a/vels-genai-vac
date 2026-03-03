# Day 03: Creating APIs with FastAPI

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
# To run this: uvicorn 05_fastapi_tutorial:app --reload

from fastapi import FastAPI
from typing import Optional

# 1. Create an instance of the FastAPI class
app = FastAPI()

# 2. Define a "Path Operation" (Route)
# The @app.get("/") decorator tells FastAPI that the function below 
# is in charge of handling requests that go to the "/" path using a GET operation.
@app.get("/")
def read_root():
    """Basic root endpoint returning a greeting."""
    return {"message": "Welcome to the Day 03 FastAPI Tutorial!"}

# 3. Path Parameters
# You can define parameters in the path using curly braces {}.
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Endpoint that takes a path parameter 'item_id'."""
    return {"item_id": item_id, "description": f"This is data for item {item_id}"}

# 4. Query Parameters
# When you declare function parameters that are not part of the path, 
# they are automatically interpreted as "query" parameters.
@app.get("/greet")
def greet_user(name: str, age: Optional[int] = None):
    """
    Endpoint using query parameters.
    Example: /greet?name=Dhanush&age=25
    """
    greeting = f"Hello {name}!"
    if age:
        greeting += f" You are {age} years old."
    return {"greeting": greeting}

# 5. Simple Post Request
# Note: In a real app, you would use Pydantic models for request bodies.
@app.post("/submit")
def submit_data(data: dict):
    """Endpoint to demonstrate a POST request receiving JSON data."""
    return {"status": "success", "received_data": data}

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    print("Visit http://127.0.0.1:8000 in your browser.")
    print("Check out the auto-generated documentation at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
