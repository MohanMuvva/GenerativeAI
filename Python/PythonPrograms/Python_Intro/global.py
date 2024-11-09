# Global variable
counter = 0

# Function using various types of parameters
def process_data(a, b=10, *args, **kwargs):
    global counter  # Use the global keyword to modify the global variable
    
    # Lambda function for addition
    add = lambda x, y: x + y
    result = add(a, b)  # Use lambda to add two numbers
    print(f"Sum of {a} and {b}: {result}")
    
    # Use *args for variable-length arguments
    print("Additional positional arguments:", args)
    
    # Use **kwargs for keyword arguments
    if 'operation' in kwargs:
        operation = kwargs['operation']
        if operation == "increment":
            counter += 1  # Increment the global counter
        elif operation == "decrement":
            counter -= 1  # Decrement the global counter
        print(f"Operation: {operation}, Global counter: {counter}")
    
    # Return a custom message
    return f"Processed data: {a}, {b}, {args}, {kwargs}"

# Function call with various arguments
result = process_data(5, 20, "extra1", "extra2", operation="increment")
print(result)  # Output of the function

# Another function call
result = process_data(15, operation="decrement", extra_info="info")
print(result)

# Using the global variable outside
print(f"Final global counter value: {counter}")

# Using a lambda function to calculate square
square = lambda x: x * x
print(f"Square of 5: {square(5)}")

