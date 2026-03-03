# Day 03: Reusable Code (Functions)

# 1. Basic Function
# A function is a block of code which only runs when it is called.
def greet_user():
    """Prints a simple greeting."""
    print("Hello! Welcome to Day 03 of Python NLP.")

# Calling the function
greet_user()

# 2. Function with Parameters
# You can pass data, known as parameters, into a function.
def personalized_greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}! Let's learn about Python functions.")

personalized_greet("Student")

# 3. Function with Return Values
# To let a function return a value, use the return statement.
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add_numbers(5, 7)
print(f"The sum of 5 and 7 is: {result}")

# 4. Reusable Logic Example
def format_text(text):
    """A helper function to clean and capitalize text."""
    clean_text = text.strip().capitalize()
    return clean_text

raw_string = "   python is awesome   "
formatted = format_text(raw_string)
print(f"Original: '{raw_string}'")
print(f"Formatted: '{formatted}'")
