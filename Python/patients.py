import pandas as pd

df = pd.read_csv('patient_data.csv')
print(df.head(5))

avgbmi = df["bmi"].mean()
print(f"The average bmi is {avgbmi:.2f}kg/m²")

hbp_count = df[df["blood_pressure"]>140].shape[0]
print(f"The number patients with high blood pressure is (bp > 140mmHg):{hbp_count}")

opa = df["age"].max()
print(f"The oldest patient age is:{opa}")

def categorize_patient(row):
    if 18.5 <= row["bmi"] <= 24.9 and row["blood_pressure"] <= 140:
        return "Healthy"
    else:
        return "At Risk"

df["Category"] = df.apply(categorize_patient, axis=1)

df.to_csv("processed_patient_data.csv", index=False)
print("Processed data has been saved to 'processed_patient_data.csv'.")

