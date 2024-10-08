# student_grade_management_system
Student Grade Management System
This project involves creating a system to manage student grades using Python. The goal is to store and manage student names, subjects, and grades in a dictionary, allowing calculations of average grades and generating a report of students’ performance.

Key Concepts
Dictionaries: Used to store student information, including names, subjects, and grades.
Lists: Used to manage subjects and grades for each student.
Tuples: Can be used to handle student information in an immutable form if needed.
Project Breakdown
Data Structure:

Use a dictionary where the key is the student's name and the value is another dictionary with subjects as keys and grades as values.
Features:

Add a Student: Add a student’s name along with subjects and corresponding grades.
Update Grades: Update the grades for a specific subject.
Calculate Average Grades: Calculate the average grade for each student.
Generate a Report: Generate a report showing each student's name, their subjects, grades, and average grade.
Functions:

Add Student: Adds a new student to the system.
Update Grades: Updates the grade for a specific subject for a student.
Calculate Average: Calculates the average grade for each student.
Generate Report: Generates and prints a performance report for all students.


Explanation
add_student Function: Adds a new student with an empty dictionary for subjects and grades.
add_grade Function: Adds or updates the grade for a specific subject for the given student.
calculate_average Function: Computes the average grade for a student by summing all grades and dividing by the number of subjects.
generate_report Function: Iterates through all students and their grades, printing out each student’s subjects and grades along with their average.
Running the Program
When you run the program, it will display a menu with options to add students, add/update grades, calculate the average grade, generate a report, or exit the program. You can interact with the program by entering the corresponding numbers to perform each action.

This system provides a basic structure for managing student grades, making it a great project to practice Python data structures such as dictionaries, lists, and tuples.