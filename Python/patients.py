import pandas as pd

# Load patient data
df = pd.read_csv('patient_data.csv')
print(df.head(5))

# Calculate average BMI
avgbmi = df["bmi"].mean()
print(f"The average BMI is {avgbmi:.2f} kg/m²")

# Count patients with high blood pressure
hbp_count = df[df["blood_pressure"] > 140].shape[0]
print(f"The number of patients with high blood pressure (BP > 140 mmHg): {hbp_count}")

# Find the oldest patient
opa = df["age"].max()
print(f"The oldest patient's age is: {opa}")

# Categorize patients
def categorize_patient(row):
    if 18.5 <= row["bmi"] <= 24.9 and row["blood_pressure"] <= 140:
        return "Healthy"
    else:
        return "At Risk"

df["Category"] = df.apply(categorize_patient, axis=1)

# Save processed data
df.to_csv("processed_patient_data.csv", index=False)
print("Processed data has been saved to 'processed_patient_data.csv'.")
