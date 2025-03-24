# file handling
# read() = read the entire file
# open() = open the file
# close() = close the file

# 1. open file to read
file = open("sets/main.py", "r")
content = file.read()
print(content)
file.close()

# 2. open file to write
file = open("file_handling/write.md", "w")
file.write("Developer")
file.close() 

# 3. open file to append
file = open("file_handling/write.md", "a")
file.write("\n Web Developer")
file.close()

# 4. open file to read line by line
file = open("sets/main.py", "r")
print(file.readline()) # read first line
print(file.readlines()) # read all lines in list
file.close()

# binary file
file = open("picture.jpg", "rb")
content = file.read()
print(content)
file.close()

# os = To check if file exists
import os
if os.path.exists("sets/main.py"):
    print("File exists")
else:
    print("File does not exists")

# tell() = tells the current position of the cursor
file = open("file_handling/main.py", "r") 
print(file.tell())  
print(file.readline())  
print(file.tell())  
file.close()


# seek() = change the position of the cursor
file = open("file_handling/main.py", "r")
file.seek(10) # move cursor to 10th position
print(file.readline())
file.close()

# strip() = remove white spaces 
text = "  Hello World    "
print(text.strip())

file = open("file_handling/main.py", "r")
line = file.readline().strip()
print(line)
file.close()

# with statement
with open("controlflow_loops/for_loop.py", "r") as file:
    print(file.readline())