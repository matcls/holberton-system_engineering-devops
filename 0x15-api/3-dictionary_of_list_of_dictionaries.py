#!/usr/bin/python3
"""Return information about employees TO-DO list.

Using https://jsonplaceholder.typicode.com/ API.
"""


def do_request():
    """Request TODO list from all employees using the REST API.

    Returns:
        String: Completed/Total tasks
    """
    import requests

    url = "https://jsonplaceholder.typicode.com/"
    users_info = requests.get(url + "users").json()

    for user in users_info:
        tasks = requests.get(url + "todos",
                             params={"userId": user.get("id")}).json()

    return users_info, tasks


def export_all_to_json(users_info, tasks):
    """Export the empployees TODO data to a JSON format file."""
    import json

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{
                  "task": task.get("title"),
                  "completed": task.get("completed"),
                  "username": user.get("username")
                  } for task in tasks]
            for user in users_info}, jsonfile)


if __name__ == "__main__":
    employees_data = do_request()
    export_all_to_json(*employees_data)
