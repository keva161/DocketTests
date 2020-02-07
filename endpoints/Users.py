import requests

class Users:
    def __init__(self, user):
        self.username = user.username
        self.email = user.email
        self.password = user.password
        self.token = user.generate_token()
        self.url = 'http://127.0.0.1:5000/api/Users/'

    def GetAllUsers(self):
        return requests.get(self.url, headers={'token': self.token}).status_code

    def DeleteUsers(self):
        return requests.delete(self.url, headers={'token': self.token}).text

    def UpdateUsers(self):
        return requests.post(self.url, headers=self.headers).text
