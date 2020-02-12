import requests
from Config import config


class Register:
    def __init__(self):
        self.url = config.SERVER + '/api/Register/'

    def CreateUser(self, user):
        # A token is passed back by the server if the registration is a success
        token = requests.post('http://127.0.0.1:5000/api/Register/',
                              json={'Username': user["Username"], 'Email Address': user["Email Address"],
                                    'Password': user["Password"]}).text.split()[-2][:-1]

        # A request is then made to delete the user to reset the server back to its initial state
        result = requests.delete(config.SERVER + '/api/Users/', headers={'token': token}).text

        return result
