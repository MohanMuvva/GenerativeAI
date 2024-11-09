class Patient:
    # Class Level Data Members
    hospital_name = "City Hospital"  # Shared across all patients

    def __init__(self, patient_id, name, age, disease):
        # Instance Data Members
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        print(f"Patient Record Created: {self.name}, {self.age} years old, Disease: {self.disease}")

    def display_info(self):
        # Instance Method - Display patient details
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")

    @classmethod
    def hospital_info(cls):
        # Class Level Method - Display hospital name
        print(f"Hospital Name: {cls.hospital_name}")

    @staticmethod
    def is_senior(age):
        # Static Method - Determines if the patient is a senior
        return age >= 60

    def __del__(self):
        # Destructor - Called when patient object is deleted
        print(f"Patient Record Deleted: {self.name}")

# Example Usage:

# Creating patient objects using constructor (__init__)
patient1 = Patient(1, "John Doe", 45, "Flu")
patient2 = Patient(2, "Jane Smith", 65, "Diabetes")

# Display patient details using instance method
patient1.display_info()  # Output: Displays patient1 details
patient2.display_info()  # Output: Displays patient2 details

# Display hospital information using class method
Patient.hospital_info()  # Output: Hospital Name: City Hospital

# Check if a patient is a senior using static method
print(f"Is {patient2.name} a senior? {'Yes' if Patient.is_senior(patient2.age) else 'No'}")  # Output: Yes

# Destructor (__del__) will be called when the object is deleted or program ends
del patient1  # Manually deleting patient1
