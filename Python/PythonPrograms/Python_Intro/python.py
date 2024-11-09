# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Taking user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area using the function
area = calculate_area(length, width)

# Outputting the result
print(f"The area of the rectangle is: {area}")
