from file_operations import *

file_obj = FileOperation("assign9.txt")

# Test the write_file() method
try:
    file_obj.write_file("This is assignment 9")
    print("File written successfully.")
except FileException as e:
    print("Exception occurred:", str(e))

# Test the read_file() method
try:
    content = file_obj.read_file()
    print("File content:", content)
except FileException as e:
    print("Exception occurred:", str(e))