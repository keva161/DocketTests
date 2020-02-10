from faker import Faker
import requests

# This class is responsible for generating new user objects. As well as registering the API tokens which are used in
# the tests.

class Generate(object):
    def __init__(self):
        fake = Faker()

        self.user = {
            "Username": fake.name().split(' ', 1)[0],
            "Email Address": fake.email(),
            "Password": fake.word(),
            "Todo": fake.word()
        }

    def GetUser(self):
        new_user = self.user
        return new_user

    def GetToken(self):
        token = requests.post('http://127.0.0.1:5000/api/Register/', json={'Username': self.user["Username"],'Email Address': self.user["Email Address"],'Password': self.user["Password"]}).text.split()[-2][:-1]
        return token




