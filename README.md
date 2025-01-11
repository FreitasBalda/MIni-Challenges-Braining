# Healthcare Data & Web Design Mini-Challenge Documentation

## Project Overview

This mini-challenge involves two tasks:  
1. **Python Challenge**: Processing patient health data and generating insights from a CSV file.
2. **HTML Challenge**: Designing a simple health checkup appointment form using HTML, CSS, and optional JavaScript validation.

---

## 1. Python Challenge: Patient Health Processor

### Objective:
The goal of this challenge is to write a Python program that reads a CSV file containing patient health data, processes it to generate insights, and exports the processed data to a new file. The key tasks include calculating average BMI, identifying patients with high blood pressure, finding the oldest patient, and categorizing patients based on their health status.

### Task Breakdown:
1. **Load & Display Data:**
   - The program reads the `patient_data.csv` file and displays the first 5 rows of the dataset to give an overview of the data.

2. **Data Processing & Analysis:**
   - **Average BMI:** The program calculates the average BMI of the patients.
   - **High Blood Pressure:** It identifies the number of patients with blood pressure higher than 140 mmHg.  
     **Note:** Although the task initially asked for the use of the `count()` function, I used the `.shape[0]` method to count the number of patients with high blood pressure. The `.shape[0]` returns the number of rows that meet the condition, providing the count of patients with BP > 140 mmHg.
   - **Oldest Patient:** The program identifies the oldest patient in the dataset.

3. **Export Processed Data:**
   - The program adds a new column to the dataset, classifying each patient as either **'Healthy'** or **'At Risk'** based on their BMI and blood pressure levels. The processed data is then exported to a new CSV file.

### Expected Skills:
- **File handling:** Handling CSV files using Python's built-in methods or libraries like `pandas`.
- **Basic data analysis:** Using basic functions like calculating the mean, maximum, and counting using `.shape[]` instead of `count()`.
- **Conditional logic:** Categorizing patients based on certain conditions like BMI and blood pressure.

---

## 2. HTML Challenge: Health Checkup Appointment Form

### Objective:
Design a health checkup appointment form using HTML and CSS, with optional JavaScript validation to ensure the form is filled out correctly. The form will collect essential information such as the patient's name, age, email, preferred appointment date, and health concerns.

### Task Breakdown:
1. **Create an HTML Form:**
   - The form includes fields for:
     - **Patient Name**
     - **Age**
     - **Email**
     - **Preferred Appointment Date**
     - **Health Concern** (a text area for additional comments)

2. **Form Styling:**
   - Use CSS to style the form, ensuring it is visually appealing and user-friendly. This includes applying background color, padding, and font styles.

3. **Validation (Optional):**
   - **Name Validation:** Initially, JavaScript was considered to ensure the name field is not empty, and the email field would be validated for correct format. However, this was not strictly necessary. 
     - By setting the `required` attribute at the end of the `<label>` for the name and email fields, the form automatically ensures the name field is not empty. 
     - Additionally, setting the `type="email"` for the email input field automatically handles email format validation, meaning that JavaScript validation becomes redundant for these cases. 

### Expected Skills:
- **HTML form structure:** Creating a structured form using elements like `<form>`, `<input>`, `<label>`, `<textarea>`, and `<button>`.
- **Basic CSS styling:** Styling the form to make it visually attractive and accessible.
- **Optional JavaScript validation:** Adding functionality to ensure the name field is not empty and the email is in the correct format (although it wasn't necessary in this case due to HTML form attributes).

---

## Conclusion

This mini-challenge provided an opportunity to apply Python for data processing and basic web development skills with HTML and CSS. The Python challenge focuses on handling and analyzing healthcare data, while the HTML challenge focuses on designing a simple and functional appointment form.
