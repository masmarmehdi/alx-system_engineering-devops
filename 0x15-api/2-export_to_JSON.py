#!/usr/bin/python3
""" Export API data in the JSON format """

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        for todo in todos:
            json.dump({user_id: {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }}, jsonfile)
