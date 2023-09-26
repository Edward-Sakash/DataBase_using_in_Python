import psycopg2

# 
db_host = "localhost"
db_name = "dci_db"
db_user = "postgres"
db_password = "stranger19"

def get_specialist_employee_list(salary):
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

        # Write the SQL query to fetch employees with a salary greater than the input amount
        sql_query = "SELECT Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience FROM Employee WHERE Salary > %s;"
        cursor.execute(sql_query, (salary,))

        # Fetch all records that match the criteria
        employee_records = cursor.fetchall()

        if employee_records:
            # Print the employee records
            print("Printing employees with a salary greater than {}".format(salary))
            for employee_record in employee_records:
                print("Employee Id:", employee_record[0])
                print("Employee Name:", employee_record[1])
                print("Warehouse Id:", employee_record[2])
                print("Joining Date:", employee_record[3])
                print("Specialty:", employee_record[4])
                print("Salary:", employee_record[5])
                print("Experience:", employee_record[6])
                print()  # Add an empty line for better readability

        else:
            print("No employees found with a salary greater than {}.".format(salary))

    except (Exception, psycopg2.Error) as error:
        print("Error fetching specialist employee list:", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Test the function with a salary threshold of 30000
get_specialist_employee_list(30000)