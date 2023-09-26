import psycopg2

# 
db_host = "localhost"
db_name = "dci_db"
db_user = "postgres"
db_password = "stranger19"

def create_employee(employee_sql_query):
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

        # Execute the provided SQL query to insert the new employee record
        cursor.execute(employee_sql_query)
        connection.commit()

        print("New employee added successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error creating employee:", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Test the function by adding a new employee
employee_sql_query = "INSERT INTO Employee (Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience) \
    VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"

create_employee(employee_sql_query)
