# Python String Methods Demonstration - All return new strings, original string remains unchanged
string = "Hello, World!"
print("Original String:", string)
print("Capitalized:", string.capitalize())
print("Count of 'l':", string.count('l')) # string.count(sub, start, end) counts occurrences of substring
print("Ends with 'World!':", string.endswith('World!')) # string.endswith(suffix, start, end) checks if the string ends with the given suffix
print("Find 'World':", string.find('World')) # string.find(sub, start, end) returns the lowest index of the substring difference between find() and index() is that find() returns -1 if not found, while index() raises ValueError
print("Index of 'World':", string.index('World')) # string.index(sub, start, end) returns the lowest index of the substring, raises ValueError if not found
print("Format:", string.format("Python", "is great!")) # string.format(*args, **kwargs) formats the string using the given arguments
dictionary = {"lang": "Python", "topic": "is great!"}
template = "Language: {lang}, Topic: {topic}"
print("Format Map:", template.format_map(dictionary)) # string.format_map(mapping) formats the string using the given mapping
print("Is Alphanumeric:", string.isalnum()) # string.isalnum() checks if all characters are alphanumeric
print("Is Alphabetic:", string.isalpha()) # string.isalpha() checks if all characters are alphabetic
print("Is Decimal:", string.isdecimal()) # string.isdecimal() checks if all characters are decimal digits
print("Is Digit:", string.isdigit()) # string.isdigit() checks if all characters are digits, even if they are superscripts or some unicode digits
print("Is Numeric:", string.isnumeric()) # string.isnumeric() checks if all characters are numeric, including fractions and roman numerals, fractions, and also all unicode numeric characters 
# isdecimal() ⊆ isdigit() ⊆ isnumeric()
print("Is ASCII:", string.isascii()) # string.isascii() checks if all characters are ASCII characters
print("Is Space:", string.isspace()) # string.isspace() checks if all characters are whitespace characters
print("Is Title:", string.istitle()) # string.istitle() checks if the string is in title case (first character of each word is uppercase)
print("Is Upper:", string.isupper()) # string.isupper() checks if all characters are uppercase
list1 = ["Python", "is", "great!"]
print("Join:", ", ".join(list1)) # string.join(iterable) joins the elements of the iterable with the string as a separator
print("Lowercase:", string.lower()) # string.lower() converts the string to lowercase
print("Lstrip:", string.lstrip("Hello, ")) # string.lstrip(chars) removes leading characters from the string
print("Rstrip:", string.rstrip(" World!")) # string.rstrip(chars) removes trailing characters from the string
print("Strip:", string.strip("Hello, World!")) # string.strip(chars) removes leading and trailing characters from the string
print("Partition 'World':", string.partition('World')) # string.partition(sub) splits the string into three parts of a tuple: the part before the substring, the substring itself, and the part after the substring
print("Replace 'World' with 'Python':", string.replace('World', 'Python')) # string.replace(old, new, count) replaces occurrences of old substring with new substring, count is optional
print("Split by space:", string.split()) # string.split(sep, maxsplit) splits the string into a list of substrings using the given separator, maxsplit is optional
print("Split by comma:", string.split(',')) # splits the string by comma
print("Starts with 'Hello':", string.startswith('Hello')) # string.startswith(prefix, start, end) checks if the string starts with the given prefix
print("Swapcase:", string.swapcase()) # string.swapcase() swaps the case of all characters in the string
print("Title Case:", string.title()) # string.title() converts the string to title case (first character of each word is uppercase, rest are lowercase)
print("Uppercase:", string.upper()) # string.upper() converts the string to uppercase
