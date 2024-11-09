class Animal:
    # Constructor with default parameters (acting as both default and parameterized)
    def __init__(self, name="dog", sound="Silent"):
        self.name = name
        self.sound = sound

    def Sound(self):
        print(f"The {self.name} goes '{self.sound}'.")

# Creating an object with default constructor
animal1 = Animal()
print(animal1.name)  # Output: Unknown
animal1.Sound()  # Output: The Unknown goes 'Silent'.

# Creating an object with parameterized constructor
animal2 = Animal(" ", "Meow")
print(animal2.name)  # Output: Cat
animal2.Sound()  # Output: The Cat goes 'Meow'.

class Car:
    # Constructor (initializes the object)
    def __init__(self, model, color):
        self.model = model
        self.color = color
        print(f"A new car has been created: {self.model}, {self.color}")

    # Destructor (called when the object is about to be destroyed)
    def __del__(self):
        print(f"The car {self.model} is being destroyed.")

# Creating an object
car1 = Car("Toyota", "Red")

# The object is still in use
print(f"Car model: {car1.model}, Car color: {car1.color}")

# When the program ends or when we manually delete the object, the destructor is called
del car1  # Manually deleting the object (optional)


