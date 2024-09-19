import os
from dotenv import load_dotenv
from pydentic import BaseModel, EmailStr

load_dotenv()


class AppConfig(BaseModel):
    api_key: str = os.getenv('API_KEY')
    user_name: str = os.getenv('USER_NAME')
    user_pass: str = os.getenv('USER_PASS')


app_config = AppConfig()


class User(BaseModel):
    name: str
    age: int
    email: EmailStr


user = User(name='John', age=34, email='test')


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