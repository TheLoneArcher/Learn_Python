# Main Three of String Formatting
# The % - Format Operator
print("The C Programming style of printing values like %d, %s, %c, and %.2f" % (3, "Python", 'A', 3.14159265))
# The format() Method
print("Or use the format() method to print values like {}, {second}, and {first}".format(3, first = 1, second = 2))
# F-Strings
age = 19
print(f"The format string or f strings are used extensively these days. E.g.: {'The Archer'}, {age}")

# reusing a single string for format()
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, None, "Hello World!"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("What", "if", "I", "give", "more", "than", "four", "arguments?"))
print("Using the format() method with a mix of positional and named arguments: {0}, {first}, {1}".format("one", "two", first = "three"))
data = {"name": "Alice", "age": 30, "city": "New York"}
print("Using the format() method with a dictionary: {name}, {age}, {city}".format(**data))
data_list = ["Alice", 30, "New York"]
print("Using the format() method with a list: {0}, {1}, {2}".format(*data_list))