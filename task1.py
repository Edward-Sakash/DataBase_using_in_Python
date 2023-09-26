import psycopg2

# 
db_host = "localhost"
db_name = "dci_db"
db_user = "postgres"
db_password = "stranger19"

# Establish a connection to the database
try:
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL query to get the database server version
    sql_query = "SELECT version();"

    # Execute the query
    cursor.execute(sql_query)

    # Fetch the record
    db_version = cursor.fetchone()

    # Print the database server version
    print("Database Server Version:", db_version[0])

except (Exception, psycopg2.Error) as error:
    print("Error connecting to the database:", error)

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

