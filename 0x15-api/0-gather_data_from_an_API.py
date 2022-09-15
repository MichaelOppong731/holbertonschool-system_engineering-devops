#!/usr/bin/python3
"""Python script that, using a REST API returns
information about his/her TODO list"""

import requests
from sys import argv

if __name__ == "__main__":
    done_tasks = 0
    n_tasks = 0
    tasks = []

    id_e = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{api_url}users/{id_e}").json()
    todos = requests.get(f"{api_url}users/{id_e}/todos").json()

    for x in todos:
        n_tasks += 1
        if x["completed"]:
            done_tasks += 1
            tasks.append(x["title"])

    print(f'Employee {user["name"]} is done with tasks' +
          f'({done_tasks}/{n_tasks}):')
    for t in tasks:
        print("\t", t)
