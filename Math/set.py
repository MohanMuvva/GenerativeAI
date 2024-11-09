def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_probability():
    # Set B: First 1000 odd numbers
    n = int(input("Enter a number: "))
    set_b = [2*i + 1 for i in range(n)]
    
    # Set A: Prime numbers within the range of set B
    set_a = [num for num in set_b if is_prime(num)]
    
    # Calculate probability
    probability = len(set_a) / len(set_b)
    
    return probability

# Calculate and print the probability
result = calculate_probability()
print(f"The probability P(A|B) is approximately {result:.4f}")
