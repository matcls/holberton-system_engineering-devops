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
    user_info = requests.get(url + "users/{}".format(employee_id)).json()
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    return employee_id, user_info, tasks


def export_to_csv(employee_id, user_info, tasks):
    """Export the empployee TODO data in a CSV format file."""
    import csv

    print(employee_id)
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id,
             user_info.get("name"),
             task.get("completed"),
             task.get("title")])
            for task in tasks]


if __name__ == "__main__":
    data = do_request()
    export_to_csv(*data)
