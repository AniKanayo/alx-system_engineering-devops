#!/usr/bin/python3
import requests
import sys

# Base URL of the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Get the employee ID from command line argument
if len(sys.argv) < 2:
    print("Please provide an employee ID as a command line argument.")
    sys.exit(1)
employee_id = int(sys.argv[1])

# Fetch the user details
user_response = requests.get(f"{BASE_URL}/users/{employee_id}")
user = user_response.json()
employee_name = user["name"]

# Fetch the TODO list for the employee
todos_response = requests.get(f"{BASE_URL}/todos?userId={employee_id}")
todos = todos_response.json()

# Calculate the progress of the employee
total_tasks = len(todos)
done_tasks = sum(todo["completed"] for todo in todos)

# Display the progress information
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo["completed"]:
        print(f"\t{todo['title']}")
