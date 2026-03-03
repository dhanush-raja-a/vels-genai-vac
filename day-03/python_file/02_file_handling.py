# Day 03: File Handling in Python

# 1. Reading a file using the 'with' statement
# The 'with' statement ensures that the file is closed properly after reading.
print("--- Reading entire file ---")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 2. Reading line by line
# Useful for large files.
print("\n--- Reading line by line ---")
with open("sample.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")

# 3. Writing to a file
# Use 'w' to overwrite or 'a' to append.
print("\n--- Writing to a new file ---")
output_filename = "output.txt"
with open(output_filename, "w") as file:
    file.write("This file was created using Python file handling!\n")
    file.write("Adding a second line.")

print(f"Successfully wrote to {output_filename}")

# 4. Checking if a file exists
import os
if os.path.exists("sample.txt"):
    print("\n'sample.txt' exists.")
else:
    print("\n'sample.txt' was not found.")
