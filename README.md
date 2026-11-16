# Student Management System

## Project Description

This project is a Python application that connects to a PostgreSQL database to perform CRUD (Create, Read, Update, and Delete) operations on student records. The application allows users to retrieve student information, add new students, update existing student email addresses, and delete student records from the database.

## Technologies Used

The application was developed using Python and PostgreSQL. The psycopg2 library is used to establish a connection between Python and the PostgreSQL database, while pgAdmin 4 is used to manage the database and verify changes to student records.

## Database Setup

To set up the database, PostgreSQL and pgAdmin 4 must first be installed. Open pgAdmin 4 and create a new database named student_management. Once the database is created, open the Query Tool and execute the SQL commands provided in the database/setup.sql file. This script creates the students table with the required columns and constraints and inserts the three initial student records.

To verify that the table was created and populated correctly, execute the following SQL query in pgAdmin:

SELECT * FROM students;

## How to Run the Application

Before running the application, ensure that Python and PostgreSQL are installed and that the PostgreSQL server is running. Open the project folder in VS Code or a terminal and install the required Python library using the command:

python -m pip install psycopg2-binary

Once the library is installed, run the application using:

python main.py

The application will prompt the user to enter their PostgreSQL password to establish a database connection. By default, the application retrieves and displays all student records. Other CRUD operations can be executed by calling the corresponding functions in the main section of the Python file.

## Application Functions

The application contains four functions for managing student records. The getAllStudents() function retrieves and displays all student records stored in the database. The addStudent(first_name, last_name, email, enrollment_date) function inserts a new student record using the provided information. The updateStudentEmail(student_id, new_email) function updates the email address of an existing student based on their student ID. Finally, the deleteStudent(student_id) function removes a student record from the database using the specified student ID.

Each function executes the appropriate SQL statement through the PostgreSQL connection. Changes made through the application can be verified using pgAdmin 4.

## Demonstration Video

A video demonstration showing the database setup and execution of all four CRUD functions is available at the following link:

[Insert video link here]
