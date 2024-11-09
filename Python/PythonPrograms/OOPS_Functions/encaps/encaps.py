class Patient:
    def __init__(self, name, age):
        # Public Data Members
        self.name = name
        self.age = age
        # Private Data Members (encapsulated)
        self.__medical_history = []  # Medical history should be private

    # Public method to access medical history (Getter)
    def get_medical_history(self):
        return self.__medical_history

    # Public method to modify medical history (Setter)
    def add_medical_history(self, record):
        self.__medical_history.append(record)

    # Instance method to display patient's basic info
    def display_info(self):
        print(f"Patient Name: {self.name}, Age: {self.age}")

# Example usage:

# Creating a patient object
patient1 = Patient("John Doe", 45)

# Accessing public data members
patient1.display_info()  # Output: Patient Name: John Doe, Age: 45

# Trying to access private data member (will raise an AttributeError)
# print(patient1.__medical_history)  # This will cause an error

# Using public methods to interact with private data (encapsulation)
patient1.add_medical_history("Diabetes diagnosed in 2022")
patient1.add_medical_history("Hypertension diagnosed in 2023")

# Accessing medical history through the getter method
print(patient1.get_medical_history())  
# Output: ['Diabetes diagnosed in 2022', 'Hypertension diagnosed in 2023']
