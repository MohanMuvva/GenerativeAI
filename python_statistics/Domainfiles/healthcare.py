import numpy as np

# Sample dataset of doctors and their specializations
doctors_data = [
    {"name": "Dr. Smith", "specialization": "Cardiologist"},
    {"name": "Dr. Adams", "specialization": "General Practitioner"},
    {"name": "Dr. Brown", "specialization": "Dermatologist"},
    {"name": "Dr. Johnson", "specialization": "Pediatrician"}
]

# Custom exception classes for specific healthcare-related errors
class InvalidAgeError(Exception):
    """Exception raised for invalid age input."""
    def __init__(self, age):
        self.message = f"Age '{age}' is invalid. Age must be a positive integer."
        super().__init__(self.message)

class InvalidEmailError(Exception):
    """Exception raised for invalid email input."""
    def __init__(self, email):
        self.message = f"Email '{email}' is invalid. Please provide a valid email address."
        super().__init__(self.message)

# Patient Class (Encapsulation and Abstraction)
class Patient:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.medical_history = []
        self.appointments = []
        
        # Using property to validate age
        self.validate_age(age)
        self.validate_email(email)

    def validate_age(self, age):
        """Check if the patient's age is valid."""
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
    
    def validate_email(self, email):
        """Check if the patient's email is valid."""
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise InvalidEmailError(email)

    def add_medical_record(self, diagnosis, treatment):
        """Add medical record to patient's history."""
        self.medical_history.append({
            "diagnosis": diagnosis,
            "treatment": treatment
        })

    def view_medical_history(self):
        """Return the patient's medical history."""
        return self.medical_history

    def schedule_appointment(self, doctor, date):
        """Schedule a new appointment for the patient."""
        self.appointments.append({
            "doctor": doctor,
            "date": date
        })

    def view_appointments(self):
        """Return a list of the patient's appointments."""
        return self.appointments

# Doctor class
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        """Add a patient to the doctor's list."""
        if isinstance(patient, Patient):
            self.patients.append(patient)
        else:
            raise ValueError("Only valid Patient objects can be added.")

    def view_patients(self):
        """View all patients assigned to the doctor."""
        return [f"{patient.first_name} {patient.last_name}" for patient in self.patients]

    def __repr__(self):
        return f"{self.name} ({self.specialization})"

# Helper function to handle age-related exceptions gracefully
def input_patient_data():
    """Get patient data from the user and handle invalid inputs."""
    try:
        first_name = input("Enter patient's first name: ")
        last_name = input("Enter patient's last name: ")
        age = int(input("Enter patient's age: "))
        email = input("Enter patient's email: ")

        # Create the patient object
        patient = Patient(first_name, last_name, age, email)
        return patient

    except InvalidAgeError as e:
        print(e)
    except InvalidEmailError as e:
        print(e)
    except ValueError:
        print("Age must be an integer.")

# Function to assign a doctor to a patient
def assign_doctor_to_patient(doctors, specialization, patient):
    """Assign a patient to a doctor based on their specialization."""
    for doctor in doctors:
        if doctor.specialization == specialization:
            doctor.add_patient(patient)
            print(f"Patient {patient.first_name} {patient.last_name} assigned to {doctor.name}.")
            return
    print(f"No doctor with specialization {specialization} found.")

# Create doctors from the dataset
def create_doctors_from_dataset(data):
    doctors = []
    for entry in data:
        doctor = Doctor(entry["name"], entry["specialization"])
        doctors.append(doctor)
    return doctors

# Using NumPy for patient statistics (e.g., age analysis)
def analyze_patient_ages(patients):
    """Analyze and print statistical information about patient ages."""
    ages = np.array([patient.age for patient in patients if isinstance(patient, Patient)])
    
    if len(ages) > 0:
        print(f"Mean Age: {np.mean(ages)}")
        print(f"Median Age: {np.median(ages)}")
        print(f"Age Standard Deviation: {np.std(ages)}")
        print(f"Youngest Patient Age: {np.min(ages)}")
        print(f"Oldest Patient Age: {np.max(ages)}")
    else:
        print("No patient data to analyze.")

# Business Workflow example for multiple patients
def healthcare_management():
    try:
        # Create doctor objects from the dataset
        doctors = create_doctors_from_dataset(doctors_data)

        # Display available doctors
        print("Available Doctors:")
        for doctor in doctors:
            print(doctor)

        # Ask for the number of patients to input
        n = int(input("How many patients would you like to enter? "))

        patients = []

        for _ in range(n):
            # Input patient data for each patient
            patient = input_patient_data()

            # If patient is created successfully, assign them to a doctor
            if patient:
                # Example: Assuming the patient needs a Cardiologist (this can be dynamic)
                specialization = input("Enter the doctor's specialization (e.g., Cardiologist): ")
                assign_doctor_to_patient(doctors, specialization, patient)

                # Add medical record and schedule an appointment
                diagnosis = input("Enter diagnosis: ")
                treatment = input("Enter treatment: ")
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")

                patient.add_medical_record(diagnosis, treatment)
                patient.schedule_appointment(specialization, appointment_date)

                patients.append(patient)

                # View patient's records
                print("\nMedical History:")
                for record in patient.view_medical_history():
                    print(record)

                print("\nAppointments:")
                for appointment in patient.view_appointments():
                    print(appointment)

        # View patients assigned to each doctor
        print("\nPatients assigned to each doctor:")
        for doctor in doctors:
            if doctor.patients:
                print(f"\n{doctor.name} ({doctor.specialization}):")
                for patient in doctor.view_patients():
                    print(f"  - {patient}")

        # Use NumPy to analyze patient ages
        print("\nPatient Age Analysis:")
        analyze_patient_ages(patients)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    healthcare_management()
