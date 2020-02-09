import requests

class Todo:
    def __init__(self, token):
        self.url = 'http://127.0.0.1:5000/api/Register/'
        self.token = token

    def GetAllTodoItems(self):
        result = requests.get('http://127.0.0.1:5000/api/Todo/', headers={'token': self.token}).text
        return result

    def CreateTodo(self, user):
        result = requests.post('http://127.0.0.1:5000/api/Todo/', headers={'token': self.token},
                               json={"Body": user["Todo"]}).text
        return result

    def DeleteTodo(self, user):
        # First of all we create a item to delete. We associate it with a new account for testing purposes.

        requests.post('http://127.0.0.1:5000/api/Todo/', headers={'token': self.token},
                      json={"Body": user["Todo"]})

        result = requests.delete('http://127.0.0.1:5000/api/Todo/1', headers={'token': self.token}).text
        return result

