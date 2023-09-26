import unittest
import psycopg2
from datetime import datetime

# Import functions from solutions
from task1 import read_database_version
from task2 import get_warehouse_detail, get_employee_detail
from task3 import update_employee_experience
from task4 import get_specialist_employee_list

# 
db_host = "localhost"
db_name = "dci_db"
db_user = "postgres"
db_password = "stranger19"

class TestWarehouseInfoSystem(unittest.TestCase):
    def setUp(self):
        # Establish a connection to the database before each test
        self.connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )

    def tearDown(self):
        # Close the database connection after each test
        self.connection.close()

    def test_solution_1(self):
        # Test reading the database version
        version = read_database_version(self.connection)
        self.assertTrue(version.startswith("PostgreSQL"))

    def test_solution_2(self):
        # Test getting warehouse and employee details
        warehouse_detail = get_warehouse_detail(2)
        print(warehouse_detail)
        self.assertEqual(warehouse_detail, 
            (2, 'Rewe Warehouse', 400)
        )

        employee_detail = get_employee_detail(105)
        self.assertEqual(employee_detail,(105, 'Linda', 3, datetime.date(2004, 6, 4)))
        
    def test_solution_3(self):
        # Test updating employee experience
        before_experience = update_employee_experience(101)
        self.assertIsNone(before_experience)  # Experience before update should be None

        after_experience = update_employee_experience(101)
        self.assertEqual(after_experience, 15)  # Experience after update should be 15

    def test_solution_4(self):
        # Test getting specialist employee list
        specialist_list = get_specialist_employee_list(30000)
        self.assertEqual(len(specialist_list), 2)  # There should be 2 employees

        # Check the details of the first specialist
        self.assertEqual(specialist_list[0], {
            'Employee Id': 102,
            'Employee Name': 'Michael',
            'Warehouse Id': 1,
            'Joining Date': '2018-07-23',
            'Specialty': 'Driver',
            'Salary': 30000,
            'Experience': None
        })

        # Check the details of the second specialist
        self.assertEqual(specialist_list[1], {
            'Employee Id': 108,
            'Employee Name': 'Karen',
            'Warehouse Id': 4,
            'Joining Date': '2011-10-17',
            'Specialty': 'Driver',
            'Salary': 30000,
            'Experience': None
        })

if __name__ == '__main__':
    unittest.main()

