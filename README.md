Patient Health Processor & Health Checkup Form
Overview
This project consists of two components:

Python Challenge: Patient Health Processor
A script that processes patient health data, analyzes key metrics, and categorizes patients based on their health conditions.

HTML Challenge: Health Checkup Appointment Form
A simple health checkup appointment form designed with HTML and CSS, including optional JavaScript validation for user input.

1. Python Challenge: Patient Health Processor
Features
Data Loading: Reads patient data from a CSV file.
Data Analysis:
Calculates the average BMI of patients.
Counts the number of patients with high blood pressure (BP > 140 mmHg).
Finds the oldest patient in the dataset.
Data Categorization: Adds a new column categorizing patients as 'Healthy' or 'At Risk' based on BMI and blood pressure.
Data Export: Saves the processed data to a new CSV file.
Requirements
Python 3.x
Pandas library
Install Pandas using pip:

bash
Copy code
pip install pandas
Usage
Place the patient_data.csv file in the same directory as the script.
Run the script:
bash
Copy code
python patient_data_analysis.py
The script will:

Display the first 5 rows of the data.
Print the average BMI, count of patients with high blood pressure, and the age of the oldest patient.
Save the processed data to processed_patient_data.csv.
Code Walkthrough
Python Script:

python
Copy code
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
2. HTML Challenge: Health Checkup Appointment Form
Features
A simple and user-friendly form for scheduling health checkup appointments.
Fields include:
Patient Name
Age
Email
Preferred Appointment Date
Health Concern
Basic CSS styling for visual appeal.
Optional JavaScript validation to ensure correct input.
Usage
Save the HTML code in a file named index.html.
Create a style.css file for the styling.
Open index.html in a web browser to use the form.
Code Walkthrough
HTML Code:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Checkup Appointment</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="form-container">
        <h2>Health Checkup Appointment</h2>
        <form id="appointmentForm">
            <label for="name">Patient Name</label>
            <input type="text" id="name" name="name" placeholder="Enter your name" required>

            <label for="age">Age</label>
            <input type="number" id="age" name="age" placeholder="Enter your age" required>

            <label for="email">Email</label>
            <input type="email" id="email" name="email" placeholder="Enter your email" required>

            <label for="date">Preferred Appointment Date</label>
            <input type="date" id="date" name="date" required>

            <label for="healthconcern">Health Concern</label>
            <textarea id="concern" name="healthconcern" rows="4" placeholder="Describe your health concern" required></textarea>

            <span id="errorMessage" class="error"></span>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
CSS Code (style.css):

css
Copy code
body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 0;
}

.form-container {
    max-width: 400px;
    margin: 50px auto;
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
    text-align: center;
    color: #333;
}

label {
    display: block;
    margin-top: 15px;
    font-weight: bold;
}

input, textarea, button {
    width: 100%;
    margin-top: 5px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

button {
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    font-weight: bold;
}

button:hover {
    background-color: #45a049;
}

.error {
    color: red;
    font-size: 0.9em;
}