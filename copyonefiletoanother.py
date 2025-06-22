from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Existence of the files: {exists(from_file)} and {exists(to_file)}\nIt's okay if the destination file does not exist yet.")
print(f"Copying from {from_file} to {to_file}")
with open(from_file, 'r') as in_file:
    data = in_file.read()
print(f"The input file is {len(data)} bytes long.")
with open(to_file, 'w') as out_file:
    out_file.write(data)
print(f"Copied {len(data)} bytes from {from_file} to {to_file}.")