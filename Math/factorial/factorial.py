import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python factorial.py <number>")
    sys.exit(1)

try:
    # Get the number from command-line argument
    num = int(sys.argv[1])
    
    # Calculate factorial
    result = factorial(num)
    
    # Print the result
    print(f"{num}! = {result}")
except ValueError:
    print("Please provide a valid integer as an argument.")
except RecursionError:
    print("Input is too large. Please use a smaller number.")
