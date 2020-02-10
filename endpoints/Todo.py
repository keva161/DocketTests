import requests
from Config import Config


class Todo:
    def __init__(self, token):
        self.url = Config.SERVER + '/api/Register/'
        self.token = token

    def GetAllTodoItems(self):
        result = requests.get(Config.SERVER + '/api/Todo/', headers={'token': self.token}).text
        return result

    def CreateTodo(self, user):
        result = requests.post(Config.SERVER + '/api/Todo/', headers={'token': self.token},
                               json={"Body": user["Todo"]}).text
        return result

    def DeleteTodo(self, user):
        # Creates a new todo_ item (the ID of this item will be 1)
        requests.post(Config.SERVER + '/api/Todo/', headers={'token': self.token},
                      json={"Body": user["Todo"]})

        # Request the todo_ item with the ID of 1 to be deleted.
        result = requests.delete(Config.SERVER + '/api/Todo/1', headers={'token': self.token}).text
        return result

