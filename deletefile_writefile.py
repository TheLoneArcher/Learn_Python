from sys import argv
from os import remove
if len(argv) < 2:
    print("Usage: python deletefile_writefile.py <filename>")
    exit(1)
filename = argv[1]
print(f"Erasing the file: {filename}")
print("If you don't want that, hit CTRL-C (^C) or ENTER to continue.")
input("?")
remove(filename)
filename = input("Enter the name of the file to write to: ")
print(f"File {filename} deleted successfully.")
print(f"Now, let's write to the file {filename}.")
with open(filename, 'w') as file:
    print("Type something to write to the file:")
    content = input("> ")
    file.write(content + "\n")
print(f"Content written to {filename}.")