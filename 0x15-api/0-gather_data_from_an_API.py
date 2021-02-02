#!/usr/bin/python3
"""Return information about a employee TO-DO list progress.

Using https://jsonplaceholder.typicode.com/ API.
"""


def do_request():
    """Request TODO list from a given employee id using the REST API.

    Returns:
        String: Completed/Total tasks
    """
    import requests
    from sys import argv

    if len(argv) < 2:
        return print('USAGE:', __file__, '<employee id>')

    try:
        employee_id = int(argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    url = "https://jsonplaceholder.typicode.com/"
    user_name = requests.get(url + "users/{}".format(employee_id)).json()
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [task.get("title") for task in tasks
                 if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_name.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]


if __name__ == "__main__":
    do_request()
