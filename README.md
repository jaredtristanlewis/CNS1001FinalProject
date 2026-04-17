# Clinic Patient Queue Management System

## Project Information
University of Technology, Jamaica  
CNS1001: Contemporary Programming  

**Group Members:**  
- Rochelle Mills (2301557)  
- Tyrese Buckley (2405302)  
- Jared Lewis (1006355)  
- Lloyd Cole (2409312)  
- Natovia Thompson (2407704)  
- Patrica Henderson (2106315)  

**Lecturer/Tutor:** Mr. Sheldon Gordon  

---

## Problem Statement
Many clinics experience delays and inefficiencies when handling patient queues manually. A properly implemented system is necessary to handle emergency case assessment and maintain proper patient flow management. The situation results in extended waiting periods, which decrease service excellence. This project was developed to create a simple system that allows a nurse to register patients and manage queues efficiently. The system ensures that emergency patients are prioritised while maintaining order for regular patients.

---

## Program Description
The program is a menu-driven system that a nurse uses to manage patient queues in a clinic.  

The system allows the nurse to:
- Add a patient by entering their name, age, and reason for visit  
- Identify whether the patient is an emergency case  
- Store patients in either a priority queue (emergency) or a regular queue  
- View the list of patients in the queue  
- Call the next patient based on priority  

---

## Main Features
- Add Patient  
- View Queue  
- Call Next Patient  
- Emergency handling (priority queue)  
- Input validation  

---

## Programming Concepts Used
The project demonstrates the following programming concepts:
- Functions: Used to organise code into reusable sections (e.g., add_patient, view_queue)  
- Loops: Used to create the menu system that runs continuously  
- Conditionals: Used to check emergency status and determine queue placement  
- Lists: Used to store patients in queues  
- Input Validation: Ensures correct data is entered (e.g., valid age, yes/no input)  

---

## How to Run the Program
Python environment open (VS Code)  
- Navigate to the folder where the file is saved  
- Run the program using:  

python project.py

- Follow the on-screen menu options to use the system  

---

## Sample Input

Enter patient name: Sharon
Enter patient age: 30
Enter reason for visit: Check up
Is this an emergency? (yes/no): no


---

## Sample Output

Patient Information Recorded:
Name: Sharon
Age: 30
Reason for Visit: Check up
Emergency: no


---

## Manual Testing and Validation Table

| Test Case           | Input                                   | Expected Output           | Actual Output     |
|--------------------|----------------------------------------|---------------------------|------------------|
| Valid patient      | Name: John, Age: 25, Emergency: no     | Added to regular queue    | Added correctly  |
| Emergency patient  | Name: Mary, Age: 40, Emergency: yes    | Added to priority queue   | Added correctly  |
| Invalid age        | Age: abc                               | Error message             | Error message shown |
| Empty name         | Name: ""                               | Prompt again              | Prompt displayed |

---

## Challenges Encountered and Lessons Learned

### Challenges
- Handling invalid input, such as letters instead of numbers for age  
- Understanding how to properly manage two queues (priority and regular)  
- Formatting output to display clearly  

### Lessons Learned
- Input validation is important to prevent program errors  
- Breaking the program into functions makes it easier to manage  
- Simple systems can still solve real-world problems effectively  

---

## Conclusion
The project offers an efficient solution for managing patient queues in clinic environments. The system enables nurses to enter patient information while prioritising emergency cases, resulting in better patient organisation and faster treatment for urgent cases. The project demonstrates fundamental programming principles through the development of a solution that addresses a real-world healthcare challenge.
