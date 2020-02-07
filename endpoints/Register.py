import requests

class Register:
    def __init__(self, user):
        self.username = user.username
        self.email = user.email
        self.password = user.password
        self.url = user.url

    def CreateUser(self):
        return requests.post(self.url, json={"Username": self.username, "Email Address": self.email, "Password": self.password}).text
