from sys import argv
filename = argv[1]  
txt = open(filename)  
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()  
print("Type another file name:") 
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
