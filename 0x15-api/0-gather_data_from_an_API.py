#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        if 'name' in employee_data and 'id' in employee_data:
            employee_name = employee_data['name']
            total_tasks = len(todos_data)
            completed_tasks = [task['title'] for task in todos_data if task['completed']]

            print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
            for task_title in completed_tasks:
                print(f"\t{task_title}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
