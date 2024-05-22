#!/usr/bin/python3
"""
Gather employee data from API and display TODO list progress.
"""

import sys

import requests

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_list_progress(employee_id):
    try:
        # Fetch employee details
        user_response = requests.get(f'{REST_API}/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch employee tasks
        tasks_response = requests.get(f'{REST_API}/todos?userId={employee_id}')
        tasks_response.raise_for_status()
        tasks_data = tasks_response.json()

        # Extract employee name
        employee_name = user_data.get('name')

        # Filter tasks
        total_tasks = len(tasks_data)
        completed_tasks = [task for task in tasks_data if task.get('completed')]
        number_of_completed_tasks = len(completed_tasks)

        # Display results
        print(f'Employee {employee_name} is done with tasks({number_of_completed_tasks}/{total_tasks}):')
        for task in completed_tasks:
            print(f'\t {task.get("title")}')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
