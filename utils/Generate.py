from faker import Faker
import requests

class Generate():

    def __init__(self):
        fake = Faker()
        self.url = 'http://127.0.0.1:5000/api/Register/'
        self.username = fake.name().split(' ', 1)[0]
        self.email = fake.email()
        self.password = fake.random_int(min=0, max=9999)
        self.token = None

    def generate_token(self):
        self.token = requests.post(self.url, json={'Username': self.username,'Email Address': self.email,'Password': self.password}).text.split()[-2][:-1]
        return self.token

