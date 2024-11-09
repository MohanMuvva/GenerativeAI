# Define a function with parameters
def introduce(name, age=25, *hobbies, **details):
    print(f"Hello, my name is {name} and I am {age} years old.")
    
    # Checking if any hobbies were passed using *args
    if hobbies:
        print("My hobbies are:", ", ".join(hobbies))
    
    # Checking if additional details were passed using **kwargs
    if details:
        print("Additional details:")
        for key, value in details.items():
            print(f"{key}: {value}")

# Call the function with different types of arguments

# Using positional and default argument
introduce("Alice")  # Uses the default age

print()  # For a blank line

# Using positional, default, and variable-length arguments (*args)
introduce("Bob", 30, "reading", "cycling", "swimming")

print()  # For a blank line

# Using keyword arguments and **kwargs for additional details
introduce("Charlie", 22, "gaming", city="New York", profession="Engineer")

