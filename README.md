# Patient Health Processor & Health Checkup Form

## Overview

This project consists of two components:

1. **Python Challenge: Patient Health Processor**  
   A script that processes patient health data, analyzes key metrics, and categorizes patients based on their health conditions.

2. **HTML Challenge: Health Checkup Appointment Form**  
   A simple health checkup appointment form designed with HTML and CSS, including optional JavaScript validation for user input.

---

## 1. Python Challenge: Patient Health Processor

### Features
- **Data Loading**: Reads patient data from a CSV file.
- **Data Analysis**:
  - Calculates the average BMI of patients.
  - Counts the number of patients with high blood pressure (BP > 140 mmHg).
  - Finds the oldest patient in the dataset.
- **Data Categorization**: Adds a new column categorizing patients as 'Healthy' or 'At Risk' based on BMI and blood pressure.
- **Data Export**: Saves the processed data to a new CSV file.

### Requirements
- Python 
- Pandas library

Install Pandas using pip:

```bash
pip install pandas
