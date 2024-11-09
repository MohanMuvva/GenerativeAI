# Define a string
my_string = " Hello, Python World! "

# 1. Concatenation: Joining strings
greeting = "Hello"
name = "John"
concatenated_string = greeting + ", " + name + "!"
print("Concatenated string:", concatenated_string)  # Output: Hello, John!

# 2. Slicing: Extract a part of the string
sliced_string = my_string[8:14]
print("Sliced string:", sliced_string)  # Output: Python

# 3. Uppercase/Lowercase conversion
print("Uppercase:", my_string.upper())  # Output: " HELLO, PYTHON WORLD! "
print("Lowercase:", my_string.lower())  # Output: " hello, python world! "

# 4. Replacing part of the string
replaced_string = my_string.replace("World", "Universe")
print("Replaced string:", replaced_string)  # Output: " Hello, Python Universe! "

# 5. Splitting the string into a list of words
words_list = my_string.split()
print("List of words:", words_list)  # Output: ['Hello,', 'Python', 'World!']

# 6. Joining the list back into a string
joined_string = " ".join(words_list)
print("Joined string:", joined_string)  # Output: Hello, Python World!

# 7. Trimming whitespace from the string
trimmed_string = my_string.strip()
print("Trimmed string:", trimmed_string)  # Output: "Hello, Python World!"

# 8. Finding the length of the string
print("Length of the string:", len(trimmed_string))  # Output: 19
