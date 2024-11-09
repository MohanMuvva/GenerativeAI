import math
import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is prime
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Step 1: Generate odd risk scores for 1000 patient
n = int(input("Enter a number: "))
patient_ids = list(range(1, n+1))
risk_scores = [2 * i + 1 for i in range(n)]  # First 1000 odd numbers from 1 to 1999

# Step 2: Identify patients with prime risk scores
prime_risk_patients = [score for score in risk_scores if is_prime(score)]

# Step 3: Calculate probability of selecting a patient with a prime risk score
probability_prime_risk = len(prime_risk_patients) / len(risk_scores)

# Display the results
print(f"Total number of patients: {len(risk_scores)}")
print(f"Number of patients with prime risk scores: {len(prime_risk_patients)}")
print(f"Probability of selecting a patient with a prime risk score: {probability_prime_risk:.4f}")

# Step 4: Simulate patient selection and flagging based on risk score

def simulate_patient_selection(patient_count=5):
    print("\nSimulating patient selections...")
    for _ in range(patient_count):
        # Randomly select a patient
        selected_patient = random.choice(patient_ids)
        selected_risk_score = risk_scores[selected_patient - 1]

        # Determine if the patient's risk score is prime
        if selected_risk_score in prime_risk_patients:
            print(f"Patient ID: {selected_patient}, Risk Score: {selected_risk_score} - High-Risk (Prime Score)")
        else:
            print(f"Patient ID: {selected_patient}, Risk Score: {selected_risk_score} - Normal Risk")

# Step 5: Allow simulation of multiple patient selections
simulate_patient_selection(5)
