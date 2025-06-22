from sys import argv
# script, first, second, third = argv
script, first, second, third, *rest = argv 
# or for only args first, second, third = argv[1:]
# or script, *args = argv
# argv is a list of command line arguments passed to the script
# argv[0] is the script name, argv[1] is the first argument, argv[2] is the second argument, and so on.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
