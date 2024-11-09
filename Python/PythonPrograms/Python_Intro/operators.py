# Function to demonstrate various operations
def perform_operations():
    # 1. String Operations
    user_name = input("Enter your name: ")  # User input
    greeting = "Hello, " + user_name + "!"
    print(greeting)

    # 2. List Operations
    fruits = ["apple", "banana", "cherry"]
    print("List of fruits:", fruits)

    # Adding an item to the list
    fruits.append("orange")
    print("List after append:", fruits)

    # Removing an item from the list
    fruits.remove("banana")
    print("List after removing banana:", fruits)

    # 3. Tuple Operations (Tuples are immutable, so we can only access or slice them)
    my_tuple = (10, 20, 30, 40, 50)
    print("Tuple:", my_tuple)
    print("First element of tuple:", my_tuple[0])
    print("Slice tuple (1 to 3):", my_tuple[1:4])

    # 4. Set Operations (Sets do not allow duplicates and are unordered)
    my_set = {1, 2, 3, 4, 2, 5}  # Duplicates will be automatically removed
    print("Set after creation (duplicates removed):", my_set)

    # Adding and removing from a set
    my_set.add(6)
    print("Set after adding 6:", my_set)

    my_set.remove(3)
    print("Set after removing 3:", my_set)

    # 5. File Input/Output Operations
    file_name = input("Enter the name of the file to save the output (e.g., output.txt): ")
    
    # Writing to the file
    with open(file_name, 'w') as file:
        file.write(greeting + "\n")  # Write greeting to the file
        file.write("List of fruits: " + str(fruits) + "\n")
        file.write("Tuple: " + str(my_tuple) + "\n")
        file.write("Set: " + str(my_set) + "\n")

    print(f"Data has been written to {file_name}")

    # Reading from the file
    with open(file_name, 'r') as file:
        content = file.read()
        print("\nContent of the file:")
        print(content)

# Call the function to perform operations
perform_operations()
