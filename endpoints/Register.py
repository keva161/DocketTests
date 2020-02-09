import requests

class Register:
    def __init__(self):
        self.url = 'http://127.0.0.1:5000/api/Register/'

    def CreateUser(self, user):
        print(user["Password"])
        # A token is passed back by the server if the registration is a success
        token = requests.post(self.url, json={"Username": user["Username"], "Email Address": user["Email Address"], "Password": user["Password"]}).text.split()[-2][:-1]

        # A request is then made to delete the user to reset the server back to its initial state
        result = requests.delete('http://127.0.0.1:5000/api/Users/', headers={'token': token}).text

        return result