from faker import Faker
import requests

class Generate(object):
    def __init__(self):
        fake = Faker()

        self.username = fake.name().split(' ', 1)[0]
        self.email = fake.email()
        self.password = fake.word()
        self.todo = fake.word()

    def user(self):
        user = {
            "Username": self.username,
            "Email Address": self.email,
            "Password": self.password,
            "Todo": self.todo
        }

        return user

    def token(self):
        token = requests.post('http://127.0.0.1:5000/api/Register/', json={'Username': self.username,'Email Address': self.email,'Password': self.password}).text.split()[-2][:-1]
        return token




