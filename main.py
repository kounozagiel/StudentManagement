import psycopg2
import getpass

# Ask for the PostgreSQL password when the program starts.
password = getpass.getpass("Enter PostgreSQL password: ")

# Create and return a connection to the student_management database.
def connect_db():
    return psycopg2.connect(
        dbname="student_management",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )


# Retrieve and display all student records in order of student ID.
def getAllStudents():
    try:
        # Open a database connection and a cursor to run SQL commands.
        with connect_db() as conn:
            with conn.cursor() as cur:
                # Select every student, ordered by their student ID.
                cur.execute("SELECT * FROM students ORDER BY student_id")

                # Fetch the query results and print each student.
                for student in cur.fetchall():
                    print(student)

    # Display a message if a database operation fails.
    except psycopg2.Error as error:
        print("Error retrieving students:", error)


# Insert a new student using the four provided values.
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        # Open a database connection and a cursor to run SQL commands.
        with connect_db() as conn:
            with conn.cursor() as cur:

                # Prepare an INSERT query for the new student's information.
                sql = """
                    INSERT INTO students
                    (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                """

                # Pass the values separately to safely fill the SQL placeholders.
                cur.execute(
                    sql,
                    (first_name, last_name, email, enrollment_date)
                )

        # The transaction is committed when the connection block succeeds.
        print("Student added successfully!")

    # Display a message if a database operation fails.
    except psycopg2.Error as error:
        print("Error adding student:", error)


# Change the email of the student with the specified ID.
def updateStudentEmail(student_id, new_email):
    try:
        # Open a database connection and a cursor to run SQL commands.
        with connect_db() as conn:
            with conn.cursor() as cur:

                # Update only the student whose ID matches the given value.
                sql = """
                    UPDATE students
                    SET email = %s
                    WHERE student_id = %s
                """

                cur.execute(sql, (new_email, student_id))
                # Check how many student records were updated.
                updated = cur.rowcount

        # Report whether a matching student was found.
        if updated > 0:
            print("Student email updated successfully!")
        else:
            print("Student not found.")

    # Display a message if a database operation fails.
    except psycopg2.Error as error:
        print("Error updating student:", error)


# Remove the student whose ID matches the given value.
def deleteStudent(student_id):
    try:
        # Open a database connection and a cursor to run SQL commands.
        with connect_db() as conn:
            with conn.cursor() as cur:

                # Delete only the record with the specified student ID.
                cur.execute(
                    "DELETE FROM students WHERE student_id = %s",
                    (student_id,)
                )

                # Count how many records were deleted.
                deleted = cur.rowcount

        # Report whether the deletion affected a student record.
        if deleted > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # Display a message if a database operation fails.
    except psycopg2.Error as error:
        print("Error deleting student:", error)


# Run this test call only when main.py is started directly.
if __name__ == "__main__":
    getAllStudents()