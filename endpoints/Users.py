import requests

class Users:
    def __init__(self, token):
        self.token = token
        self.url = 'http://127.0.0.1:5000/api/Users/'

    def GetAllUsers(self):
        result = requests.get(self.url, headers={'token': self.token}).status_code
        return result

    def DeleteUser(self):
        result = requests.delete(self.url, headers={'token': self.token}).text
        return result

    def UpdateUser(self, user):

        print(user["Password"])
        result = requests.put(self.url, headers={'token': self.token}, json={"Username": user["Username"], "Email Address": user["Email Address"], "Password": user["Password"]}).text
        return result