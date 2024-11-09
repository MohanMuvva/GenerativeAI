import os

# Function to read data from an input file
def read_from_file(email):
    try:
        with open(email, 'r') as file:  # Open the file in read mode
            return file.read()  # Return the contents of the file
    except FileNotFoundError:
        print(f"File '{email}' not found. Creating a new file.")
        return ""

# Function to write data to an output file
def write_to_file(email, data):
    with open(email, 'w') as file:  # Open the file in write mode
        file.write(data)  # Write the data to the file

# Function to add content to a file
def add_content_to_file(filename):
    print("Enter the content you want to add to the file.")
    print("Type 'END' on a new line when you're finished:")
    
    content = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        content.append(line)
    
    with open(filename, 'a') as file:
        file.write('\n'.join(content) + '\n')
    
    print(f"Content added to '{filename}'.")

# Main program
input_filename = "C:/Users/ASUS/Documents/email.txt"

# Read data from the input file
data = read_from_file(input_filename)

# Display current content (if any)
if data:
    print(f"Current content of '{input_filename}':")
    print(data)
    print("\n")
else:
    print("The file is currently empty.\n")

# Always offer to add content
while True:
    add_content = input("Do you want to add content? (yes/no): ").lower()
    if add_content != 'yes':
        break
    add_content_to_file(input_filename)
    data = read_from_file(input_filename)
    print("\nUpdated content:")
    print(data)
    print("\n")

print(f"Final content of '{input_filename}':")
print(data)
