import requests
from Config import Config

class Users:
    def __init__(self, token):
        self.token = token
        self.url = Config.SERVER + '/api/Users/'

    def GetAllUsers(self):
        result = requests.get(self.url, headers={'token': self.token}).text
        return result

    def DeleteUser(self):
        result = requests.delete(self.url, headers={'token': self.token}).text
        return result

    def UpdateUser(self, user):
        result = requests.put(self.url, headers={'token': self.token}, json={"Username": user["Username"], "Email Address": user["Email Address"], "Password": user["Password"]}).text
        return result