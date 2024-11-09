import os

# Function to read data from an input file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            return file.read()  # Return the contents of the file
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."

# Function to write data to an output file
def write_to_file(filename, data):
    with open(filename, 'w') as file:  # Open the file in write mode
        file.write(data)  # Write the data to the file

# Main program
# Specify the file paths directly in the code
base_path = "C:/Users/ASUS/Documents" # Adjust this to your actual base path
input_filename = os.path.join(base_path, "email.txt")
output_filename = os.path.join(base_path, "email2.txt")

# Read data from the input file

data = read_from_file(input_filename)

# Check if there was an error reading the input file
if "Error" in data:
    print(data)  # Print the error message
else:
    # Write the data to the output file
    write_to_file(output_filename, data)
    print(f"Data has been written to '{output_filename}'.")
