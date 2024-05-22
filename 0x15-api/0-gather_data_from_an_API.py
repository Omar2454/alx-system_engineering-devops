#!/usr/bin/python3
'''
Gather employee data from API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    if re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])

        try:
            # Fetch employee details
            user_response = requests.get(
                f'{REST_API}/users/{employee_id}'
            )
            user_response.raise_for_status()
            user_data = user_response.json()

            # Fetch employee tasks
            tasks_response = requests.get(
                f'{REST_API}/todos?userId={employee_id}'
            )
            tasks_response.raise_for_status()
            tasks_data = tasks_response.json()

            # Extract employee name and adjust its length if needed
            emp_name = user_data.get('name')
            if len(emp_name) > 18:
                emp_name = emp_name[:18]  # Truncate name to 18 characters

            # Filter tasks
            total_tasks = len(tasks_data)
            completed_tasks = [
                task for task in tasks_data if task.get('completed')
            ]
            number_of_completed_tasks = len(completed_tasks)

            # Display results
            print(
                f'Employee {emp_name} is done with tasks('
                f'{number_of_completed_tasks}/{total_tasks}):'
            )
            for task in completed_tasks:
                print(f'\t {task.get("title")}')

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            sys.exit(1)
    else:
        print("Employee ID must be an integer")
        sys.exit(1)
