import psycopg2

# 
db_host = "localhost"
db_name = "dci_db"
db_user = "postgres"
db_password = "stranger19"

def get_warehouse_detail(warehouse_id):
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

        # Write the SQL query to retrieve the Warehouse details based on the given Warehouse ID
        sql_query = "SELECT Warehouse_Id, Warehouse_Name, Employee_Count FROM Warehouse WHERE Warehouse_Id = %s;"

        # Execute the query with the provided warehouse ID as a parameter
        cursor.execute(sql_query, (warehouse_id,))

        # Fetch the record
        warehouse_record = cursor.fetchone()

        if warehouse_record:
            # Print Warehouse record
            print("Printing Warehouse record")
            print("Warehouse Id:", warehouse_record[0])
            print("Warehouse Name:", warehouse_record[1])
            print("Employee Count:", warehouse_record[2])
            return warehouse_record
        else:
            print("Warehouse with ID {} not found.".format(warehouse_id))

    except (Exception, psycopg2.Error) as error:
        print("Error getting Warehouse detail:", error)

    finally:
        print(warehouse_record)
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


def get_employee_detail(employee_id):
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

        # Write the SQL query to retrieve the Employee details based on the given Employee ID
        sql_query = "SELECT Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience FROM Employee WHERE Employee_Id = %s;"

        # Execute the query with the provided employee ID as a parameter
        cursor.execute(sql_query, (employee_id,))

        # Fetch the record
        employee_record = cursor.fetchone()

        if employee_record:
            # Print Employee record
            print("Printing Employee record")
            print("Employee Id:", employee_record[0])
            print("Employee Name:", employee_record[1])
            print("Warehouse Id:", employee_record[2])
            print("Joining Date:", employee_record[3])
            print("Specialty:", employee_record[4])
            print("Salary:", employee_record[5])
            print("Experience:", employee_record[6])
            return employee_record
        else:
            print("Employee with ID {} not found.".format(employee_id))

    except (Exception, psycopg2.Error) as error:
        print("Error getting Employee detail:", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Test the functions
get_warehouse_detail(2)
get_employee_detail(105)
