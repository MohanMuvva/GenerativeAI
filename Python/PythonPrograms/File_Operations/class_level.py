class Car:
    # Class Level Data Members
    company = "Toyota"  # Class-level data member (shared across all instances)

    def __init__(self, model, color):
        # Instance Data Members (unique to each object)
        self.model = model
        self.color = color
        print(f"A new car has been created: {self.model}, {self.color}")

    def instance_method(self):
        # Instance Method - operates on instance-specific data members
        print(f"The {self.color} {self.model} is driving.")

    @classmethod
    def class_level_method(cls):
        # Class-level method - operates on class-level data members
        print(f"This is a {cls.company} car.")

    @staticmethod
    def static_method(info):
        # Static Method - performs universal or utility operations
        print(f"Car information: {info}")

    def __del__(self):
        # Destructor - cleans up when the object is destroyed
        print(f"The car {self.model} is being destroyed.")

# Example usage:

# Creating an object (Instance)
car1 = Car("Corolla", "Red")

# Calling an instance method
car1.instance_method()  # Output: The Red Corolla is driving.

# Calling a class-level method
Car.class_level_method()  # Output: This is a Toyota car.

# Calling a static method
Car.static_method("Corolla, Red, 2024 model")  # Output: Car information: Corolla, Red, 2024 model.

# Destructor is called when the object is deleted or when the program ends
del car1  # Manually deleting the object (optional)
