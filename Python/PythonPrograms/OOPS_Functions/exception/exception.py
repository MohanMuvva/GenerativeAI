import sys
import os
import math
import datetime
import random
import json

class Patient:
    def __init__(self, name, doa, age):
        # Constructor to initialize patient details
        self.__name = name
        self.__doa = datetime.datetime.strptime(doa, "%d/%m/%Y")
        self.__age = age  # Initialize with the provided age
        self.__id = random.randint(1000, 9999)  # Random ID using random module

    def get_name(self):
        # Getter for name
        return self.__name

    def get_doa(self):
        return self.__doa.strftime("%d/%m/%Y")

    def set_name(self, name):
        # Setter for name
        self.__name = name

    def set_doa(self, doa):
        self.__doa = datetime.datetime.strptime(doa, "%d/%m/%Y")

    def get_age(self):
        # Getter for age
        return self.__age

    def set_age(self, age):
        # Setter for age
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer")

    def input_age(self):
        while True:
            try:
                # Asking for user input (age of the patient)
                age = int(input(f"Enter the age of patient {self.__name}: "))

                # Using if-else condition to check if age is positive
                if age > 0:
                    self.set_age(age)  # Set the age first
                    print(f"Patient {self.__name}'s age of DOA:{self.get_doa()} is: {self.__age} years")
                    break
                else:
                    print(f"Invalid input for {self.__name}: Age must be a positive number.")
            except ValueError:
                # Handling non-integer values
                print(f"Invalid input for {self.__name}: Please enter a valid number.")
            
        print(f"Patient age input process completed for {self.__name}.\n")

    def to_json(self):
        return json.dumps({
            "name": self.__name,
            "doa": self.get_doa(),
            "age": self.__age,
            "id": self.__id
        })

    def calculate_next_appointment(self):
        # Using math module to calculate next appointment
        days_to_add = math.ceil(self.__age / 10) * 30  # Older patients have appointments further apart
        next_appointment = self.__doa + datetime.timedelta(days=days_to_add)
        return next_appointment.strftime("%d/%m/%Y")

def main():
    # Using OS module to get and display current working directory
    print(f"Current working directory: {os.getcwd()}")

    patients = [
        Patient("John Doe", "12/03/2015", 45),
        Patient("Jane Smith", "12/07/2016", 54)
    ]

    for patient in patients:
        patient.input_age()
        print(f"Next appointment for {patient.get_name()}: {patient.calculate_next_appointment()}")
        print(f"Patient JSON: {patient.to_json()}")

    # Using sys module to exit the program
    sys.exit("Program completed successfully")

if __name__ == "__main__":
    main()