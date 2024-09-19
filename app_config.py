import os
from dotenv import load_dotenv

load_dotenv()


class UserInfo:
    def __init__(self):
        self.api = os.environ.get('API_KEY')
        self.name = os.environ.get('USER_NAME')
        self.password = os.environ.get('USER_PASS')

    def get_api(self):
        return self.api

    def get_name(self):
        return self.name

    def get_pass(self):
        return self.password