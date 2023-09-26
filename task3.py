import psycopg2
from datetime import datetime

# 
db_host = "localhost"
db_name = "dci_db"
db_user = "postgres"
db_password = "stranger19"

def update_employee_experience(employee_id):
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Get the current employee record
        get_employee_query = "SELECT Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience FROM Employee WHERE Employee_Id = %s;"
        cursor.execute(get_employee_query, (employee_id,))
        employee_record = cursor.fetchone()

        if employee_record:
            # Get the joining date of the given employee
            joining_date = employee_record[3]

            # Calculate the experience in years
            today_date = datetime.now().date()
            experience_years = today_date.year - joining_date.year

            # Update the experience for the given employee
            update_experience_query = "UPDATE Employee SET Experience = %s WHERE Employee_Id = %s;"
            cursor.execute(update_experience_query, (experience_years, employee_id))
            connection.commit()

            # Print the updated Employee record
            print("BEFORE")
            print("Printing Employee record")
            print("Employee Id:", employee_record[0])
            print("Employee Name:", employee_record[1])
            print("Warehouse Id:", employee_record[2])
            print("Joining Date:", employee_record[3])
            print("Specialty:", employee_record[4])
            print("Salary:", employee_record[5])
            print("Experience:", employee_record[6])
            print("AFTER")
            print("Printing Employee record")
            print("Employee Id:", employee_id)
            print("Employee Name:", employee_record[1])
            print("Warehouse Id:", employee_record[2])
            print("Joining Date:", employee_record[3])
            print("Specialty:", employee_record[4])
            print("Salary:", employee_record[5])
            print("Experience:", experience_years)

        else:
            print("Employee with ID {} not found.".format(employee_id))

    except (Exception, psycopg2.Error) as error:
        print("Error updating Employee experience:", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

def read_database_version(connection):
    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Write the SQL query to get the database version
        sql_query = "SELECT version();"
        cursor.execute(sql_query)

        # Fetch the database version
        version = cursor.fetchone()[0]

        return version

    except (Exception, psycopg2.Error) as error:
        print("Error reading database version:", error)
        return None

    finally:
        if cursor:
            cursor.close()


# Test the function
update_employee_experience(101)